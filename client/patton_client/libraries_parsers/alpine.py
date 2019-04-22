import re
import logging

from typing import List, Dict

from patton_client import PattonRunningConfig, PCException

log = logging.getLogger("patton-cli")

FIND_REGEX = re.compile(
    r'''(ii[ ]+)([\w\-\+\.]+)([\:\w]*)*([ ]+)([\w\.\:\-\+\~]+)''')


def alpine_parser(lines: str, config: PattonRunningConfig) -> Dict:

    results = {}

    content = lines.splitlines()

    if "Installed:" not in content[0] and "Available:" not in content[0]:
        raise PCException("Input data is not in 'apk version' format")

    # Try to check dpkg format
    for library in content[1:]:

        if library.startswith("."):
            continue

        # Try to find the start point of version in text. i.e:
        # libressl2.5-libssl-2.5.4-r0 -> start point is: 19
        pre = ""
        for i, x in enumerate(library):
            if pre == "-" and x.isdigit():
                break
            else:
                pre = x

        dep_name = library[:i - 1]

        token_slitted = library.find("<")
        if not token_slitted:
            token_slitted = library.find("=")

        dep_version = library[i:token_slitted].strip()
        results[dep_name] = dep_version

    return results
