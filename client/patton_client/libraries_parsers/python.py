import urllib
import logging

from typing import Dict
from xml.etree import ElementTree
from urllib.request import urlopen

from patton_client import PattonRunningConfig, PCException

log = logging.getLogger("patton-cli")


def get_last_version_package(package_name):

    try:
        with urlopen(f"https://pypi.python.org/simple/{package_name}/") as f:
            tree = ElementTree.parse(f)
    except urllib.error.HTTPError:
        return None

    results = set()
    for a in tree.iter('a'):
        if not a.text.endswith("tar.gz"):
            continue

        lib_version = a.text[a.text.rfind("-") + 1:].replace(".tar.gz", "")
        results.add(lib_version)

    return max(results)


def python_parser(lines: str, config: PattonRunningConfig) -> Dict:
    results = {}

    for dep in lines.splitlines():
        _dep = dep.strip()

        try:
            found_dep_name, found_dep_version, *_ = _dep.split("==",
                                                               maxsplit=2)
            results[found_dep_name] = found_dep_version
        except ValueError as e:
            found_dep_version = get_last_version_package(dep)

            if not found_dep_version:
                message = f"Package '{dep}' not found in Pypi servers"

                if config.skip_on_fail:
                    log.info(message)
                else:
                    raise PCException(message)

            results[dep] = found_dep_version

    return results
