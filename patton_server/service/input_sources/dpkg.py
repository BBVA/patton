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
}

RELEASE_REGEX = re.compile(r'''([\d\.]+)(-)([\d]+)''')


def dpkg_builder(package: List[Dict[str, str]]) -> str:
    """Return the full text query"""
    query = set()
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
            library = library[len("lib") + 1:]

        # python3-* -> *
        if library.startswith(("python3-", "python2-")):
            library = library[len("python3-") + 1:]

        # *-examples
        if any(library.endswith(x) for x in (
                "-examples", "-doc", "-src", "-dbg"
        )) or any(x in library for x in (
                "-dev", "-core", "-data", "-extra", "-utils", "-runtime",
                "-common"
        )):
            continue

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
        # has_sep = version.find("-")
        # if has_sep:
        #     _re = RELEASE_REGEX.search(version)
        #     if _re:
        #         _, _, release = _re.groups()
        #
        #         version = version[:has_sep] + "\:" + release

        # Case to parse:
        #   1.3.dfsg2-1build1
        # Valid result
        #   1.3:rc2

        # --------------------------------------------------------------------------
        # Build queries
        # --------------------------------------------------------------------------
        full_text_query = f"{library.lower()}:* & {version.lower()}:*"

        q_select = f"(Select '{library.lower()}:{version.lower()}', " \
                   f"v.cve, " \
                   f"v.cpe, v.cvss, " \
                   f"v.summary " \
                   f"from prodvuln_view " \
                   f"as v where to_tsvector('english', v.cpe) @@ to_tsquery(" \
                   f"'{full_text_query}') order by v.cvss desc limit 10) "

        query.add(q_select)

    q = " UNION ALL ".join(query)
    return q
