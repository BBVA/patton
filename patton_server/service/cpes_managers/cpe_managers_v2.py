from typing import List, Dict
from collections import defaultdict

from ..input_sources import specific_build_db_query


async def _do_query(db_pool, query: str) -> Dict[str, List]:
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


async def _do_query_detailed(db_pool, query: str) -> Dict[str, List]:
    results = dict()

    map_cpe_cves = defaultdict(list)

    async with db_pool.acquire() as connection:
        async with connection.cursor() as cur:
            await cur.execute(query)

            async for row in cur:
                try:
                    map_cpe_cves[row[2]].append({
                        "cve": row[1],
                        "score": row[3],
                        "summary": row[4],
                    })
                    results[row[0]]["cpes_temp"].append(row[2])
                    results[row[0]]["cves"].append(
                        {
                            "cve": row[1],
                            "score": row[3],
                            "summary": row[4]
                        }
                    )
                except KeyError:
                    results[row[0]] = dict()
                    results[row[0]]["cpes_temp"] = []
                    results[row[0]]["cves"] = []

                    results[row[0]]["cpes_temp"].append(row[2])
                    results[row[0]]["cves"].append(
                        {
                            "cve": row[1],
                            "score": row[3],
                            "summary": row[4]
                        }
                    )
    # Add mapping
    updated_results = {}
    for dep_name, dep_values in results.items():
        new_values = {
            "cpes": [
                {
                    "cpe": cpe,
                    "cves": map_cpe_cves[cpe]
                }
                for cpe in dep_values["cpes_temp"]
            ],
            "cves": dep_values["cves"]
        }

        updated_results[dep_name] = new_values

    return updated_results


# --------------------------------------------------------------------------
# CPE Calls
# --------------------------------------------------------------------------
# def _build_cpe_query(packages_versions: Dict) -> str:
#     search_method = packages_versions.get("method", "auto")
#     version_source = packages_versions.get("source", "auto")
#
#     # for i, lib in enumerate(packages_versions.get("libraries", [])):
#     #
#     #     library = lib.get("library", None)
#     #     version = lib.get("version", None)
#     #
#     #     if not library or not version:
#     #         continue
#     #
#     #     lib_and_package = f"{library.lower()}:{version.lower()}"
#     #
#     #     # full_text_query = f"({library.lower()}:* & {version.lower()}:*)"
#     #     full_text_query = specific_build_db_query(version_source,
#     #                                               library,
#     #                                               version)
#     #
#     #     q_select = f"(Select '{lib_and_package}' as t{i}, v.cve as cpe_{i}, " \
#     #                f"v.cpe as cpe_{i}, v.cvss as cvss_{i}, " \
#     #                f"v.summary as summary_{i} from " \
#     #                f"prodvuln_view " \
#     #                f"as v where to_tsvector('english', v.cpe) @@ to_tsquery(" \
#     #                f"'{full_text_query}') order by v.cvss desc limit 10) "
#     #
#     #     query.append(q_select)
#
#     return specific_build_db_query(source=version_source,
#                                    package=packages_versions.get("libraries",
#                                                                  []))
#

async def query_cpe(db_pool,
                    arr: Dict,
                    detailed_cpe: int = False,
                    max_concurrent_analyze: int = 300) -> Dict[str, List]:
    # --------------------------------------------------------------------------
    # Build query
    # --------------------------------------------------------------------------
    search_method = arr.get("method", "auto")
    version_source = arr.get("source", "auto")
    query = specific_build_db_query(
        source=version_source,
        package=arr.get("libraries", []),
        maximum_concurrent_packages_to_analyze=max_concurrent_analyze)

    # --------------------------------------------------------------------------
    # Launch it
    # --------------------------------------------------------------------------
    if detailed_cpe == 1:
        return await _do_query_detailed(db_pool, query)
    else:
        return await _do_query(db_pool, query)

