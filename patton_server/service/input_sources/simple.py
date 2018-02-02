from typing import List, Dict


def simple_builder(package: List[Dict[str, str]]) -> str:
    """Return the full text query"""

    query = set()
    for lib in package:

        library = lib.get("library", None)
        version = lib.get("version", None)

        if not library or not version:
            continue

        full_text_query = f"{library.lower()}:* & {version.lower()}:*"

        q_select = f"(Select '{library.lower()}:{version.lower()}', " \
                   f"v.cve, " \
                   f"v.cpe, v.cvss, " \
                   f"v.summary from " \
                   f"prodvuln_view " \
                   f"as v where to_tsvector('english', v.cpe) @@ to_tsquery(" \
                   f"'{full_text_query}') order by v.cvss desc limit 10) "

        query.add(q_select)

    return " UNION ALL".join(query)
