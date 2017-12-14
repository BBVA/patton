from sqlalchemy.dialects.postgresql import insert
from lxml import etree

from ..config import DOWNLOAD_FOLDER
from . import models
from .database import session_ctx


def cpe_loader():
    with session_ctx() as session, \
         open(f'{DOWNLOAD_FOLDER}/official-cpe-dictionary_v2.3.xml', 'r') as markup:

        root = etree.parse(markup)

        session.execute(
            insert(models.Prod),
            models.Prod.loader_map(root)
        )

        session.execute(
            insert(models.ProdReference),
            models.ProdReference.loader_map(root)
        )

        session.execute(
            insert(models.Cpe23),
            models.Cpe23.loader_map(root)
        )

        print('cpe_loaded')


def cve_loader():
    with session_ctx() as session:
        for year in range(2002, 2018):
            with open(f'{DOWNLOAD_FOLDER}/nvdcve-2.0-{year}.xml', 'r') as markup:

                print(f'loading year: {year}')
                root = etree.parse(markup)

                session.execute(
                    insert(models.Vuln),
                    models.Vuln.loader_map(root)
                )

                session.execute(
                    insert(models.VulnReference),
                    models.VulnReference.loader_map(root)
                )

                session.execute(
                    insert(models.VulnScore),
                    models.VulnScore.loader_map(root)
                )

                session.execute(
                    insert(models.Prod).values(
                        models.VulnProduct.preload_fk_map(root)
                    ).on_conflict_do_nothing()
                )

                session.execute(
                    insert(models.VulnProduct),
                    models.VulnProduct.loader_map(root)
                )

    print('cve_loaded')
