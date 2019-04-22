from typing import List, Dict

from patton_client import PattonRunningConfig

from .simple import simple_parser
from .dpkg import dpkg_parser
from .python import python_parser
from .alpine import alpine_parser
from .golang import golang_parser


DEPENDENCIES_PARSERS = {
    'auto': simple_parser,
    'simple_parser': simple_parser,
    'dpkg': dpkg_parser,
    'python': python_parser,
    'alpine': alpine_parser,
    'golang': golang_parser
}


def parse_dependencies(dependencies: List[List[str]],
                       patton_config: PattonRunningConfig) -> Dict:
    """This function try to find the better function to parser input banners
    and parse it"""

    result = {}

    for source_type, source_content in dependencies:

        # Select parser
        parser = DEPENDENCIES_PARSERS[patton_config.source_type]

        if not source_content:
            continue

        if source_type == "cli_input":
            fixed_source = "\n".join(source_content)
        else:
            fixed_source = source_content

        result.update(parser(fixed_source, patton_config))

    return result
