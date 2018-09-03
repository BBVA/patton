from typing import Union, Dict, List

from patton_server.exceptions import PSException

from .dpkg import dpkg_builder
from .simple import simple_builder
from .alpine import alpine_builder
from .maven import maven_builder

DEFAULT_BUILDER = simple_builder

SOURCES = {
    # Ubuntu-like parsers
    'dpkg': dpkg_builder,
    'ubuntu': dpkg_builder,
    'debian': dpkg_builder,

    # Alpine-like
    'alpine': alpine_builder,
    'apk': alpine_builder,

    # Java
    'java': maven_builder,
    'maven': maven_builder
}


def specific_build_db_query(source: str,
                            package: List[Dict[str, str]],
                            maximum_concurrent_packages_to_analyze: int = 300)\
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
        return simple_builder(package, maximum_concurrent_packages_to_analyze)

    try:
        r = SOURCES[source](package, maximum_concurrent_packages_to_analyze)
        return r
    except KeyError:
        r = DEFAULT_BUILDER(package, maximum_concurrent_packages_to_analyze)
    finally:
        return r
