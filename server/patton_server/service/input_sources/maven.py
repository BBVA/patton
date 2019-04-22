import slugify

from typing import List, Dict


def maven_builder(package: List[Dict[str, str]],
                  max_packages_to_analyze: int = 300) -> str:
    """Return the full text query"""

    query = set()
    packages_to_analyze = 0
    for lib in package:

        library = slugify.slugify(lib.get("library", None))
        version = slugify.slugify(lib.get("version", None), separator=".")

        # ---------------------------------------------------------------------
        # Cleaning version
        # ---------------------------------------------------------------------
        # For versions formats like: 5.0.0-FINAL, 1.0.0RELEASE, 1.0.0-RELEASE
        # To -> 5.0.0 | 1.0.0 | 1.0.0
        ending_position = None
        for i, letter in enumerate(version):
            _letter: str = letter
            if not _letter.isdigit() and not _letter == ".":
                ending_position = i
                break

        if ending_position is not None:
            version = version[:ending_position]

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
