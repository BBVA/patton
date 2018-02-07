from typing import List, Dict


def simple_builder(package: List[Dict[str, str]],
                   max_packages_to_analyze: int = 300) -> str:
    """Return the full text query"""

    query = set()
    packages_to_analyze = 0
    for lib in package:

        library = lib.get("library", None)
        version = lib.get("version", None)

        if not library or not version:
            continue

        if packages_to_analyze > max_packages_to_analyze:
            break

        q_select = f"(Select '{library.lower()}:{version.lower()}', " \
                   f"v.cve, " \
                   f"v.cpe, v.cvss, " \
                   f"v.summary from " \
                   f"prodvuln_view as v " \
                   f"where to_tsvector('english', v.cpe) @@ to_tsquery(" \
                   f"'{library.lower()}:D') AND " \
                   f"to_tsvector('english', v.cpe) @@ to_tsquery(" \
                   f"'{version.lower()}:D') " \
                   f"order by v.cpe desc, v.cvss desc limit 10) "

        query.add(q_select)

        packages_to_analyze += 1

    return " UNION ALL".join(query)
