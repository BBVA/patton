from typing import List, Dict, Set

from patton_client import PattonRunningConfig

from .nmap import parse_from_continuous as nmap_continuous, \
    parse_from_file as nmap_file

BANNER_PARSERS = {
    'auto': (None, None),
    'nmap': (nmap_file, nmap_continuous)
}


def parse_banners(banners: List[List[str]],
                  patton_config: PattonRunningConfig) -> Set:
    """This function try to find the better function to parser input banners
    and parse it"""

    result = set()

    for source_type, source_content in banners:
        if source_type == "file":
            result.update(nmap_file(source_content))

    return result


__all__ = ("BANNER_PARSERS", "parse_banners")
