import time
import gzip
import shutil
import logging
import datetime
import requests
import tempfile
import os.path as op

from tqdm import tqdm
from lxml import etree
from typing import Set, List
from urllib.request import urlopen
from collections import defaultdict

from . import models

log = logging.getLogger("patton-server")

LAST_YEAR_CVE = datetime.datetime.now().year


def download_assets(download_path: str,
                    only_last_cve: bool = False):
    #
    # Download CVE
    #
    files = set()

    # Add CPE
    files.add("https://static.nvd.nist.gov/feeds/xml/cpe/dictionary/"
              "official-cpe-dictionary_v2.3.xml.gz")

    if only_last_cve:
        files.add("https://static.nvd.nist.gov/feeds/xml/cve/2.0/nvdcve-2.0-"
                  "recent.xml.gz")
    else:
        files.update([f"https://static.nvd.nist.gov/feeds/xml/cve/2.0/"
                      f"nvdcve-2.0-{x}.xml.gz"
                      for x in range(2002, LAST_YEAR_CVE + 1)])

    log.info(f"Donwloading CPE and CVE files")
    for f in files:
        results_file_name = f[f.rfind("/") + 1:].replace(".gz", "")

        # Check if file is already downloaded
        if op.exists(
                op.join(download_path, results_file_name)
        ):
            log.debug(f"File {results_file_name} is in cache. Skipping")
            continue

        # Download info
        file_size = int(urlopen(f).info().get('Content-Length', -1))
        header = {"Range": "bytes=%s-%s" % (0, file_size)}

        # Try to download for 5 times
        for x in range(5):
            try:
                file_raw = requests.get(f,
                                        headers=header,
                                        stream=True)
            except requests.exceptions.ReadTimeout:
                log.critical(f"Timeout when try to get file: {f}. Sleeping 5 "
                             f"seconds")
                time.sleep(5)

        # ---------------------------------------------------------------------
        # Download file and save in a temporal file until it'll be uncompressed
        # ---------------------------------------------------------------------
        with tempfile.NamedTemporaryFile() as tmp_download_file:

            # Download and save the file in a tmp file
            with open(tmp_download_file.name, "wb") as \
                    tmp_download_file_handler:

                progress_bar = tqdm(total=file_size,
                                    initial=0,
                                    unit='B',
                                    unit_scale=True,
                                    desc="    > {}".format(f.split('/')[-1]))

                for chunk in file_raw.iter_content(chunk_size=1024):
                    # Update progress bar

                    if chunk:  # filter out keep-alive new chunks
                        tmp_download_file_handler.write(chunk)
                        progress_bar.update(1024)

                progress_bar.close()

            # Uncompress in a file with the same name but without .gz
            log.debug(f"Uncompressing and saving file: {results_file_name}")
            with gzip.open(tmp_download_file.name, 'rb') as f_in, \
                    open(op.join(download_path,
                                 results_file_name), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)


async def create_view(db_pool):
    # Update Views
    q_views = "CREATE MATERIALIZED VIEW prodvuln_view AS SELECT " \
              "vuln.id as CVE, prod.id as CPE, vuln.cvss_score AS CVSS, " \
              "vuln.summary as SUMMARY " \
              "FROM vuln JOIN vuln_product ON vuln.id = vuln_product.vuln_id "\
              "JOIN prod ON prod.id = vuln_product.prod_id; " \
              "CREATE INDEX tsv_cpe ON prodvuln_view USING " \
              "gin(to_tsvector('english', cpe));"

    log.info("Creating view and indexes")
    async with db_pool.acquire() as con:
        await con.execute(q_views)


async def refresh_view(db_pool):
    # Update Views
    q_views = "REFRESH MATERIALIZED VIEW prodvuln_view;"
    log.info("Refreshing database view. This could take some time")
    async with db_pool.acquire() as con:
        await con.execute(q_views)


async def update_indexes(db_pool):
    # Update Views
    q_views = "REINDEX table prodvuln_view;"

    log.info("Refreshing database indexes. This could take some time")
    async with db_pool.acquire() as con:
        await con.execute(q_views)


async def cpe_update(db_pool, download_path: str):
    with open(f'{download_path}/official-cpe-dictionary_v2.3.xml', "r") as f:
        root = etree.parse(f)

    log.info("Start loading CPE")

    async with db_pool.acquire() as con:
        existing_cpe = set(x[0] for x in
                           await con.fetch("Select DISTINCT id from prod;"))

    log.debug("Start loading CPE:Prod")
    file_products = models.Prod.loader_map(root, existing_cpe)

    if file_products:
        async with db_pool.acquire() as con:
            await con.copy_records_to_table("prod",
                                            records=file_products)

        log.debug("Start loading CPE:ProdReference")
        d = models.ProdReference.loader_map(root)
        async with db_pool.acquire() as con:
            await con.copy_records_to_table("prod_reference",
                                            records=d)

        log.debug("Start loading CPE:Cpe23")
        d = models.Cpe23.loader_map(root)
        async with db_pool.acquire() as con:
            await con.copy_records_to_table("cpe23",
                                            records=d)

    log.info('cpe_loaded')


async def _update_cves(cve_file: str,
                       db_pool) -> Set[str]:

    log.info(f'loading CVEs from file: {cve_file}')
    with open(cve_file, 'r') as markup:
        root = etree.parse(markup)

    # ---------------------------------------------------------------------
    # DB queries
    # ---------------------------------------------------------------------
    log.debug("Start loading CVE:Vulns")
    async with db_pool.acquire() as con:
        existing_cves = set(x[0] for x in
                            await con.fetch("Select DISTINCT id from vuln;"))

    cves = models.Vuln.loader_map(root, existing_cves)
    async with db_pool.acquire() as con:
        await con.copy_records_to_table("vuln",
                                        records=cves)

    # Get existing CPE inside CVEs
    log.debug("Start loading missing CPE in CVE files")
    async with db_pool.acquire() as con:
        existing_cpes = set(x[0] for x in
                            await con.fetch("Select DISTINCT id from prod;"))

    d = models.VulnProduct.preload_fk_map(root, existing_cpes)
    async with db_pool.acquire() as con:
        await con.copy_records_to_table("prod",
                                        records=d)

    log.debug("Start loading CVE:VulnProduct")
    d = models.VulnProduct.loader_map(root)
    async with db_pool.acquire() as con:
        await con.copy_records_to_table("vuln_product",
                                        records=d)

    return set(x[0] for x in cves)


async def first_populate_cve_loader(db_pool, download_path: str,):
    total_cves_loaded = set()

    for year in range(2002, LAST_YEAR_CVE):
        file_path = f'{download_path}/nvdcve-2.0-{year}.xml'
        total_cves_loaded.update(await _update_cves(file_path,
                                                    db_pool))


async def update_cves(db_pool, download_path: str) -> set:
    """Update database and return news CVE than doesn't exits in before"""

    return await _update_cves(f'{download_path}/nvdcve-2.0-recent.xml',
                              db_pool)


async def build_cves_cve_rel(db_pool, cves: List[str]):
    """From CVEs, get relations: CPE <1---N> CVE"""
    results = defaultdict(list)

    cve_search_query = " or ".join(f"cve = '{c}'" for c in cves)

    q = f"﻿select cpe, cve from prodvuln_view where {cve_search_query};"

    async with db_pool.acquire() as connection:
        async with connection.cursor() as cur:
            await cur.execute(q)

            async for row in cur:
                results[row[0]].append(row[1])

    return results
