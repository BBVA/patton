from typing import List, Dict


def _build_cpe_query(packages_versions: List[List[str]]) -> str:
    query = []

    for i, (lang, library, version) in enumerate(packages_versions):
        lib_and_package = f"{library.lower()}:{version.lower()}"

        full_text_query = f"({library.lower()}:* & {version.lower()}:*)"

        q_select = f"(Select '{lib_and_package}' as t{i}, v.cve as cpe_{i}, " \
                   f"v.cpe as cpe_{i}, v.cvss as cvss_{i} from " \
                   f"prodvuln_view " \
                   f"as v where to_tsvector('english', v.cpe) @@ to_tsquery(" \
                   f"'{full_text_query}') order by v.cvss desc limit 10) "

        query.append(q_select)

    return " UNION ALL".join(query)


async def query_cpe(db_pool, arr: List[List[str]]) -> Dict[str, Dict]:
    query = _build_cpe_query(arr)

    results = dict()

    async with db_pool.acquire() as connection:
        async with connection.cursor() as cur:
            await cur.execute(query)

            async for row in cur:
                try:
                    results[row[0]]["cpes"].append(row[2])
                    results[row[0]]["cves"].append(
                        {
                            "cve": row[1],
                            "score": row[3],
                        }
                    )
                except KeyError:
                    results[row[0]] = dict()
                    results[row[0]]["cpes"] = []
                    results[row[0]]["cves"] = []

                    results[row[0]]["cpes"].append(row[2])
                    results[row[0]]["cves"].append(
                        {
                            "cve": row[1],
                            "score": row[3],
                        }
                    )

    return results
