from typing import Union, Dict, List

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

SQL_WHERE = ''


def specific_build_db_query(source: str, package: List[Dict[str, str]]) \
        -> Union[str, PSException]:
    """
    input format for libraries:

    [
        {
            "library": "django",
            "version": "1.2"
        },
        {
            "library": "flask",
            "version": "1.00.1"
        }
    ]
    """
    if not package:
        return {}

    if not source:
        return simple_builder(package)

    try:
        r = SOURCES[source](package)
        return r
    except KeyError:
        raise PSException(f"Invalid source. "
                          f"Valid sources are: {SOURCES.keys()}")
