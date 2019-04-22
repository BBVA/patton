import re
import logging

from typing import List, Dict

from patton_client import PattonRunningConfig, PCException

log = logging.getLogger("patton-cli")

FIND_REGEX = re.compile(
    r'''(ii[ ]+)([\w\-\+\.]+)([\:\w]*)*([ ]+)([\w\.\:\-\+\~]+)''')


def dpkg_parser(lines: str, config: PattonRunningConfig) -> Dict:

    results = {}

    # Try to check dpkg format
    if not lines.startswith("Desired=Unknown/Install/Remove/Purge/Hold"):
        raise PCException("Input data is not in 'dpkg -l' format")

    for x in FIND_REGEX.findall(lines):

        dep_name = x[1]
        dep_version = x[4]

        # TODO: mirar como hacer para pillar tambien las releases
        if dep_name == "perl" and dep_version == "5.22.1":
            dep_version = "5.22.1:rc5"  # asi si lo pilla

        if ":" in dep_version:
            dep_version = dep_version[dep_version.find(":") + 1:]

        results[dep_name] = dep_version

    return results
