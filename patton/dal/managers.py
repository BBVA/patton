from typing import List, Dict

from sqlalchemy.sql import text

from .database import session_ctx


search_statement = text(
    """
    select  prod.id,
            vuln.id,
            vuln.published,
            vr.reference_type,
            vr.href,
            vr.href_description,
            vs.score,
            vs.access_vector,
            vs.source

        from public.prod as prod

        join public.vuln_product as vp on prod.id = vp.prod_id
        join public.vuln as vuln on vuln.id = vp.vuln_id
        join public.vuln_reference as vr on vr.vuln_id = vuln.id
        join public.vuln_score as vs on vs.vuln_id = vuln.id

        where prod.id @@ to_tsquery(:query);
    """)


def query_cpe(prod: str, version: str) -> List[list]:
    with session_ctx() as session:
        result = session.execute(
            search_statement,
            {'query': f'{prod} & {version}'}
        )

    return [i for i in result]


def batch_query_cpe(arr: List[List[str]]) -> Dict[str, List]:
    return {
        f'{prod}:{version}': query_cpe(prod, version)
        for prod, version in arr
    }
