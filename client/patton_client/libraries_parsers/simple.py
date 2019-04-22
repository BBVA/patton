import logging

from typing import Dict

from patton_client import PattonRunningConfig, PCException

log = logging.getLogger("patton-cli")


def _find_separator(text: str) -> str:
    """
    This function try to find a valid separator for a library:version.

    Depending of the source of data, separators should be different and it
    need to choose the most convenient.

    For example, a library with format:

    little-cms 2.2.9,

    The can see that there are 2 valid separators: space and '-', but the
    only valid is the space.
    """

    if "==" in text:
        return "=="
    elif " " in text:
        return " "
    elif "-" in text:
        return "-"
    elif ":" in text:
        return ":"
    else:
        raise PCException("Can't find a valid library token splitter")


def simple_parser(lines: str, config: PattonRunningConfig) -> Dict:
    results = {}

    for dep in lines.splitlines():
        _dep = dep.strip()
        separator = _find_separator(_dep)

        try:
            found_dep_name, found_dep_version, *_ = _dep.split(separator,
                                                               maxsplit=2)

            results[found_dep_name] = found_dep_version
        except ValueError as e:

            if config.skip_on_fail:
                log.info("Invalid separator format for dep {dep}. Skipping")
            else:
                raise PCException("Dependencies have invalid format. "
                                  "Format must be: <library>:<version>, "
                                  "i.e: django:1.2")

    return results
