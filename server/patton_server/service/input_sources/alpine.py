import re

from typing import List, Dict

RELEASE_REGEX = re.compile(r'''([\d\.]+)(-)([\d]+)''')

UNNECESSARY_FILES = {
    "base-files",
    "ca-certificates",
    "apk",
    "e2fslibs",
    "e2fsprogs",
    "ed",
    "eject",
    "file",
    "hostname",
    "locales",
    "man-db",
    "manpages",
    "mlocate",
    "sed",
    "grep",
    "ed",
    "awk",
    "gawk",
    "vim-common",
    "at",
}

OPTIMUM_LIMIT_FOR_ADD_RELEASE = 80


def alpine_builder(package: List[Dict[str, str]],
                   max_packages_to_analyze: int = 300) -> str:
    """Return the full text query"""
    query = set()
    packages_to_analyze = 0
    total_packages = len(package)
    for lib in package:
        library = lib.get("library", None)
        version = lib.get("version", None)

        if not library or not version and library not in UNNECESSARY_FILES:
            continue

        # --------------------------------------------------------------------------
        # Usually this query is very heavy. We'll try to do thinker removing
        # unnecessary libraries
        # --------------------------------------------------------------------------

        # lib* -> *
        if library.startswith("lib"):
            library = library[len("lib"):]

        # python2|python3-* -> *
        if library.startswith(("python3-", "python2-")):
            library = library[len("python3-"):]

        # py2|py3-* -> *
        if library.startswith(("py3-", "py2-")):
            library = library[len("py2-"):]

        # py-* -> *
        if library.startswith("py-"):
            library = library[len("py-"):]

        # *-examples
        if any(library.endswith(x) for x in (
                "-examples", "-doc", "-src", "-dbg"
        )) or any(x in library for x in (
                "-dev", "-core", "-data", "-extra", "-utils", "-runtime",
                "-common"
        )):
            continue

        library_full_text = f'{library.lower()}:D'

        # --------------------------------------------------------------------------
        # Filter for versions
        # --------------------------------------------------------------------------
        #
        # 2.5.4-r0 -> 2.5.4:r0
        revision_index = version.find("-r")
        if revision_index:
            _version = version[:revision_index]
            _release = version[revision_index:].replace("-r", "rc")
            if total_packages < OPTIMUM_LIMIT_FOR_ADD_RELEASE:
                version_full_text = f"({_version}:D | {_release}:*)"
            else:
                version_full_text = f"{version}:D"
        else:
            version_full_text = f"{version}:D"

        if packages_to_analyze > max_packages_to_analyze:
            break

        # --------------------------------------------------------------------------
        # Build queries
        # --------------------------------------------------------------------------
        full_text_query = f"{library_full_text} & {version_full_text.lower()}"

        q_select = f"(Select '{library.lower()}:{version.lower()}', " \
                   f"v.cve, " \
                   f"v.cpe, v.cvss, " \
                   f"v.summary " \
                   f"from prodvuln_view as v " \
                   f"where to_tsvector('english', v.cpe) @@ to_tsquery(" \
                   f"'{library_full_text}') AND " \
                   f"to_tsvector('english', v.cpe) @@ to_tsquery(" \
                   f"'{version_full_text.lower()}') " \
                   f"order by v.cpe desc, v.cvss desc limit 10) "

        query.add(q_select)

        packages_to_analyze += 1

    q = " UNION ALL ".join(query)
    return q
