from typing import Union

from patton_server.exceptions import PSException

from .dpkg import dpkg_builder
from .simple import simple_builder

SOURCES = {
    # Ubuntu-like parsers
    'dpkg': dpkg_builder,
    'ubuntu': dpkg_builder,
    'debian': dpkg_builder,

    # Default
    'auto': simple_builder,
    'simple': simple_builder
}


def build_full_text(source: str, library: str, version: str) \
        -> Union[str, PSException]:

    if not version or not source or not library:
        return simple_builder(library, version)

    try:
        return SOURCES[source](library, version)
    except KeyError:
        raise PSException(f"Invalid source. "
                          f"Valid sources are: {SOURCES.keys()}")
