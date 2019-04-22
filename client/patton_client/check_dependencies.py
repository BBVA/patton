import logging

from typing import Set, List, Union

from patton_client import PattonRunningConfig, check_dependencies_from_api, \
    get_data_from_sources

from .libraries_parsers import parse_dependencies


log = logging.getLogger("patton-cli")


def check_dependencies(patton_config: PattonRunningConfig):

    dependencies = get_data_from_sources(patton_config,
                                         dependency_or_banner="banner")

    dependencies = parse_dependencies(dependencies, patton_config)

    if len(dependencies) > 300:
        log.error(f"You're trying to test '{len(dependencies)}' dependencies. "
                  f"Patton server is limited (by default) to the first 300 "
                  f"libraries. Only first 300 will be tested. ")

    if len(dependencies) > 100:
        log.error("Patton server has less accuracy when you try more than 100"
                  "libraries per request. It's advisable to not exceed this "
                  "limit if you want more accurate results")

    # -------------------------------------------------------------------------
    # Is a continuous check?
    # -------------------------------------------------------------------------
    results = check_dependencies_from_api(dependencies,
                                          patton_config=patton_config)

    #
    # Display results
    #
    results.display(patton_config.display_format)

    #
    # Dump results to file
    #
    results.dump()


__all__ = ("check_dependencies", )
