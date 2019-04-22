import os
import sys
import select
import asyncio
import os.path as op

from typing import List, Set

from patton_client import PattonRunningConfig, PattonResults, PCException
from patton_client.api_queires import check_dependencies_in_patton, \
    check_banners_in_patton


def check_dependencies_from_api(deps: Set[str],
                                patton_config: PattonRunningConfig) \
        -> PattonResults:
    loop = asyncio.get_event_loop()

    results = loop.run_until_complete(
        check_dependencies_in_patton(deps, patton_config)
    )

    return PattonResults.from_api(results, patton_config)


def check_banners_from_api(banners: List[str],
                           patton_config: PattonRunningConfig) \
        -> PattonResults:
    loop = asyncio.get_event_loop()

    results = loop.run_until_complete(
        check_banners_in_patton(banners, patton_config)
    )

    return PattonResults.from_api(results, patton_config)


def get_data_from_sources(patton_config: PattonRunningConfig,
                          dependency_or_banner: str = "dependency") \
        -> List[str]:
    """This function try to get data from different sources:

    - command line arguments
    - from external input file
    - from stdin

    Return a list with the content of all of collected data. A list element by
    each input data found.

    :param dependency_or_banner: allowed values are: ["dependency" | "banner"]
    :type dependency_or_banner: str
    """

    def _read_stdin() -> str:

        # Read input with 5 sec timeout
        while sys.stdin in select.select([sys.stdin], [], [], 2)[0]:
            line = sys.stdin.readline()
            if line:
                yield line
            else:  # an empty line means stdin has been closed
                return

    # --------------------------------------------------------------------------
    # Find data source
    # --------------------------------------------------------------------------
    dependencies = []

    # Data from command line from user?
    if patton_config.nargs_input:
        if dependency_or_banner == "banner":
            dependencies.append(["cli_input", patton_config.nargs_input])
        else:
            dependencies.extend(patton_config.nargs_input)

    # Data form stdin input ?
    if not sys.stdin.isatty():
        input_read = "".join(list(_read_stdin()))

        # YES => Data from stdin
        if input_read:
            if dependency_or_banner == "banner":
                dependencies.append(["stdin", input_read])
            else:
                dependencies.extend(input_read.splitlines())

    # Data from file?
    if patton_config.data_from_file:

        f = op.abspath(op.join(op.abspath(os.getcwd()),
                               patton_config.data_from_file))

        # YES => dependencies from file
        with open(f, "r") as f:
            if dependency_or_banner == "banner":
                dependencies.append(["file", f.read()])
            else:
                dependencies.extend(f.read().splitlines())

    # NO data from any other source => Continuous check selected?
    if not dependencies and not patton_config.follow_checking:

        # NO data source found => Error! We need some data!
        raise PCException("You need to specify andy dependency "
                          "from any kind of source: stdin, "
                          "file of cli")

    return dependencies


__all__ = ("check_dependencies_from_api", "check_banners_from_api",
           "get_data_from_sources")
