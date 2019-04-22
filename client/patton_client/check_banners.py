import logging

from typing import Set, List, Union

from patton_client import PattonRunningConfig, check_banners_from_api, \
    get_data_from_sources

from patton_client.banners_services import parse_banners

log = logging.getLogger("patton-cli")


def _check_banners(banners: Union[Set[str], List[str]],
                   patton_config: PattonRunningConfig):

    results = check_banners_from_api(banners,
                                     patton_config=patton_config)

    #
    # Display results
    #
    results.display(patton_config.display_format)


def check_banners(patton_config: PattonRunningConfig):

    # -------------------------------------------------------------------------
    # Is a continuous check?
    # -------------------------------------------------------------------------
    if patton_config.follow_checking:
        # dependencies = get_data_from_sources(patton_config)
        pass
    else:
        input_banners = get_data_from_sources(patton_config,
                                              dependency_or_banner="banner")

        # Select the banner type parser and get dependencies
        parsed_banners = parse_banners(input_banners, patton_config)

        _check_banners(parsed_banners, patton_config)


__all__ = ("check_banners", )
