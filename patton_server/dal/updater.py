import logging
import tempfile
import asyncio

import aiohttp
import asyncpg

from patton_server.dal.database import create, check_if_db_already_created
from patton_server.dal.loader import first_populate_cve_loader, \
    cpe_update, download_assets, update_cves, create_view, update_indexes, \
    refresh_view, build_cves_cve_rel

log = logging.getLogger("patton-server")


async def notify_weeb_hook(url, info):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}/patton/webhook') as resp:
            if resp.status == 200:
                return None
            else:
                return await resp.text()


async def _update_db(path: str,
                     db_url: str,
                     init_db: bool = False,
                     web_hook: str = None):
    db_pool = await asyncpg.create_pool(dsn=db_url,
                                        max_queries=200000,
                                        min_size=20,
                                        max_size=50)

    # Ensure database exits before try to populate
    if init_db:
        log.info("Ensuring database is ready")
        if not await check_if_db_already_created(db_pool):
            log.debug("Creating DB")
            await create(db_pool)

        # Populate
        log.debug("Populating DB")
        download_assets(path,
                        only_last_cve=False)
        await cpe_update(db_pool, path)
        await first_populate_cve_loader(db_pool, path)

        # Creating tables and idexes
        await create_view(db_pool)

    else:
        if not await check_if_db_already_created(db_pool):
            log.error("! You need to initializate database firt of update it")
            return

        # Download only the incremental CVE file
        download_assets(path,
                        only_last_cve=True)
        #
        new_cves = await cpe_update(db_pool, path)
        await update_cves(db_pool, path)
        await refresh_view(db_pool)
        await update_indexes(db_pool)

        if web_hook:
            cve_cpe_relation = await build_cves_cve_rel(new_cves)
            oks = await notify_weeb_hook(cve_cpe_relation)
            if not oks:
                print(f"Couldn't notify the weebhook. Error: {oks}")


def update_db(**kwargs):
    tmp_dir = kwargs.get("PATTON_DOWNLOAD_FOLDER", None)
    init_db = kwargs.get("INIT_DB", False)
    db_url = kwargs.get("PATTON_DB_URL", False)
    web_hook = kwargs.get("WEB_HOOK", False)

    # If recreate options was chosen -> drop && create database
    if not tmp_dir:
        with tempfile.TemporaryDirectory(dir=tmp_dir) as f:
            asyncio.get_event_loop().run_until_complete(
                _update_db(f,
                           db_url,
                           init_db,
                           web_hook))
    else:
        asyncio.get_event_loop().run_until_complete(
            _update_db(tmp_dir,
                       db_url,
                       init_db,
                       web_hook))


__all__ = ("update_db", )
