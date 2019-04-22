import logging
import argparse

from patton_client import PattonRunningConfig, \
    PCException, PCServerResponseException, check_dependencies, \
    check_banners, PattonResults
from patton_client.banners_services import BANNER_PARSERS
from patton_client.libraries_parsers import DEPENDENCIES_PARSERS

logging.basicConfig(format='[LOG] %(message)s')
log = logging.getLogger("patton-cli")


def argument_parser():
    sources = set()
    sources.update(DEPENDENCIES_PARSERS.keys())
    sources.update(BANNER_PARSERS.keys())

    patton_cli = "patton"

    examples = f"""
Examples:

  * Checking specific library and output as table:
    > {patton_cli} django:1.2 flask:1.1.0
  
  * Checking Python installed dependencies and output as CSV:
    > pip freeze | {patton_cli} -F csv
    or
    > {patton_cli} -F csv -i requirements.txt
  
  * Checking ubuntu dependencies display as table and dump in json file:
    > dpkg -l | {patton_cli} -e dpkg -F table -o results.json
"""

    parser = argparse.ArgumentParser(
        description='Patton-cli',
        epilog=examples,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'INPUT_LIST', nargs="*"
    )

    parser.add_argument('-v',
                        action='count',
                        dest="LOG_LEVEL",
                        help='log level',
                        default=3)

    parser.add_argument('--patton-host',
                        dest="PATTON_HOST",
                        help='patton server host',
                        default="patton.owaspmadrid.org:8000")

    parser.add_argument('-F', '--display-format',
                        dest="DISPLAY_FORMAT",
                        help='display format options',
                        choices=("table", "json", "csv"),
                        default="table")

    parser.add_argument('-q', '--quiet',
                        dest="QUIET_MODE",
                        help='do not display any information in stdout',
                        action="store_true",
                        default=False)

    parser.add_argument('-i', '--from-file',
                        dest="FROM_FILE",
                        help="output file for results",
                        default=None)

    parser.add_argument('-o', '--output-file',
                        dest="OUTPUT_FILE",
                        help=f"results file. formats: "
                             f"{', '.join(PattonResults.ALLOWED_DUMP_FORMATS)}",
                        default=None)

    parser.add_argument('-e', '--source-type',
                        dest="SOURCE_TYPE",
                        help="use specific source parser",
                        choices=sources,
                        default="auto")

    parser.add_argument('-s', '--skip-on-fail',
                        dest="SKIP_ON_FAIL",
                        action="store_true",
                        help="doesn't abort execution on dependency check "
                             "fail",
                        default=False)

    working_mode = parser.add_argument_group("Working modes")
    working_mode.add_argument('-D', '--dependency',
                              dest="WORKING_MODE",
                              action="store_true",
                              help="check libraries and versions (default)",
                              default=True)
    working_mode.add_argument('-B', '--banner',
                              dest="WORKING_MODE",
                              action="store_true",
                              help="check banners (currently experimental)",
                              default=False)

    banner_parser = parser.add_argument_group("Specific option for banners")
    banner_parser.add_argument('-t', '--banner-type',
                               dest="BANNER_TYPE",
                               help='http, ftp, ...-',
                               choices=BANNER_PARSERS.keys(),
                               default=False)
    banner_parser.add_argument('-f', '--follow',
                               dest="FOLLOW_CHECKING",
                               help='read from stdin and do '
                                    'a continuously check',
                               action="store_true",
                               default=False)

    return parser


def _get_log_level(config: PattonRunningConfig, level: int) -> int:

    # If quiet mode selected -> decrease log level
    if config.quiet_mode:
        input_level = 100
    else:
        input_level = level * 10

        if input_level > 50:
            input_level = 50

        input_level = 60 - input_level

    return input_level


def main():
    parser = argument_parser()
    parsed_cmd = parser.parse_args()

    patton_config = PattonRunningConfig.from_argparser(parsed_cmd)

    log.setLevel(_get_log_level(
        patton_config,
        parsed_cmd.LOG_LEVEL))

    #
    # Check dependencies
    #
    if parsed_cmd.WORKING_MODE:
        try:
            check_dependencies(patton_config)

            print(f'\nPatton Server used => "{parsed_cmd.PATTON_HOST}"\n')

        except (PCException, PCServerResponseException) as e:
            print(f"\n[!] {e}\n")
            exit(-1)

    #
    # Check banners
    #
    else:
        try:
            check_banners(patton_config)
        except (PCException, PCServerResponseException) as e:
            print(f"\n[!] {e}\n")
            exit(-1)


if __name__ == '__main__':
    main()
