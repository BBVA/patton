import re

from typing import List, Dict

UNNECESSARY_FILES = {
    "base-files",
    "ca-certificates",
    "cloud-guest-utils",
    "cloud-init",
    "cloud-initramfs-copymods",
    "command-not-found",
    "command-not-found-data",
    "debianutils",
    "debconf",
    "debconf-i18n",
    "distro-info-data",
    "dpkg",
    "e2fslibs",
    "e2fsprogs",
    "ed",
    "eject",
    "file",
    "fonts-ubuntu-font-family-console",
    "geoip-database",
    "hostname",
    "init-system-helpers",
    "install-info",
    "keyboard-configuration",
    "language-selector-common",
    "linux-base",
    "locales",
    "man-db",
    "manpages",
    "mime-support",
    "mlocate",
    "readline-common",
    "rename",
    "sed",
    "grep",
    "ed",
    "awk",
    "gawk",
    "software-properties-common",
    "sosreport",
    "ubuntu-minimal",
    "ubuntu-release-upgrader-core",
    "ubuntu-standard",
    "unattended-upgrades",
    "update-manager-core",
    "update-notifier-common",
    "uuid-runtime",
    "vim-common",
    "at"
}

RELEASE_REGEX = re.compile(r'''([\d\.]+)(-)([\d]+)''')
OPTIMUM_LIMIT_FOR_ADD_RELEASE = 80


def dpkg_builder(package: List[Dict[str, str]],
                 max_packages_to_analyze: int = 300) -> str:
    """Return the full text query"""
    query = set()
    packages_to_analyze = 0
    total_packages = len(package)
    for lib in package:
        library = lib.get("library", None)
        version = lib.get("version", None)

        if not library or not version or library in UNNECESSARY_FILES:
            continue

        # --------------------------------------------------------------------------
        # Usually this query is very heavy. We'll try to do thinker removing
        # unnecessary libraries
        # --------------------------------------------------------------------------

        # lib* -> *
        if library.startswith("lib"):
            library = library[len("lib"):]

        # python3-* -> *
        if library.startswith(("python3-", "python2-")):
            library = library[len("python3-"):]

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
        has_two_points = version.find(":")
        if has_two_points:
            version = version[has_two_points + 1:]

        # Case to parse:
        #   5.22.1-9ubuntu0.2
        # Valid result:
        #   5.22.1:rc9
        # TODO: Improve that: if we uncomment bellow code query to database is
        # TODO: really slow
        release = None
        has_sep = version.find("-")
        if has_sep:
            _re = RELEASE_REGEX.search(version)
            if _re:
                version, _, release = _re.groups()

        if release:
            # With more than 100 elements, PostgresSQL Query is very slow
            if total_packages < OPTIMUM_LIMIT_FOR_ADD_RELEASE:
                version_full_text = f"({version}:D | {release}:*)"
            else:
                version_full_text = f"{version}:D"
        else:
            version_full_text = f"{version}:D"

        # Case to parse:
        #   1.3.dfsg2-1build1
        # Valid result
        #   1.3:rc2

        if packages_to_analyze > max_packages_to_analyze:
            break

        # --------------------------------------------------------------------------
        # Build queries
        # --------------------------------------------------------------------------
        full_text_query = f"{library_full_text} & {version_full_text}"

        if library == "at":
            print(library)

        q_select = f"(Select '{library.lower()}:{version.lower()}', " \
                   f"v.cve, " \
                   f"v.cpe, v.cvss, " \
                   f"v.summary " \
                   f"from prodvuln_view as v " \
                   f"where to_tsvector('english', v.cpe) @@ to_tsquery(" \
                   f"'{library_full_text}') AND " \
                   f"to_tsvector('english', v.cpe) @@ to_tsquery(" \
                   f"'{version_full_text}')  " \
                   f"order by v.cpe desc, v.cvss desc limit 10) "

        query.add(q_select)

        packages_to_analyze += 1

    q = " UNION ALL ".join(query)
    return q
