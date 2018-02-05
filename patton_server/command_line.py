import logging
import argparse

logging.basicConfig(format='[%(levelname)-s] %(message)s',
                    level=logging.INFO)
log = logging.getLogger("patton-server")


def argument_parser():
    parser = argparse.ArgumentParser(
        description='Retrieve stdin and analyze it for vulnerabilities'
    )
    parser.add_argument(
        '-v',
        action='count',
        dest="LOG_LEVEL",
        help='log level',
        default=3
    )
    parser.add_argument(
        '-C', '--connection-string',
        dest="PATTON_DB_URL",
        help='connection string to the database',
        default="postgres://postgres:postgres@localhost:5432/patton"
    )

    subparsers = parser.add_subparsers(help='Options', dest="option")

    # --------------------------------------------------------------------------
    # Parser: serve
    # --------------------------------------------------------------------------
    serve = subparsers.add_parser('serve', help='launch patton service')
    serve.add_argument(
        '-l', '--listen', help='listen address. Default: 127.0.0.1',
        default="127.0.0.1"
    )
    serve.add_argument(
        '-p', '--port',
        help='listen port for service. Default: 8000',
        type=int,
        default=8000
    )
    serve.add_argument(
        '-w', '--workers', help='workers. Default: 1',
        default=1
    )
    serve.add_argument(
        '-b', '--backlog', help='maximum concurrent connections',
        default=512
    )
    serve.add_argument(
        '-d', '--debug', help='enable debug. Default: disabled',
        default=0
    )
    serve.add_argument(
        '-M', '--maximum-concurrent',
        help="maximum packages to analyze (DON'T TOUCH THIS OPTION!)",
        default=300
    )

    # --------------------------------------------------------------------------
    # Parser: update
    # --------------------------------------------------------------------------
    init_db = subparsers.add_parser('init-db', help='create and populate DB')
    init_db.add_argument(
        '-D', '--download-folder',
        dest="PATTON_DOWNLOAD_FOLDER",
        help='download folder for temporal data',
        default=None
    )

    update = subparsers.add_parser('update-db', help='update CVE & CPE info')
    update.add_argument(
        '-W', '--web-hook',
        dest="WEB_HOOK",
        help='url to notify new loaded CVEs',
        default=None
    )
    update.add_argument(
        '-D', '--download-folder',
        dest="PATTON_DOWNLOAD_FOLDER",
        help='download folder for temporal data',
        default=None
    )

    return parser.parse_args()


def _get_log_level(level: int) -> int:

    # If quiet mode selected -> decrease log level
    input_level = level * 10

    if input_level > 50:
        input_level = 50

    return 60 - input_level


def main():

    parsed_cmd = argument_parser()

    # set logger level
    log.setLevel(_get_log_level(parsed_cmd.LOG_LEVEL))

    # Config in dict format
    config = dict(parsed_cmd._get_kwargs())

    #
    # Run actions
    #
    if parsed_cmd.option == "serve":
        from patton_server.service.make_web_app import make_app

        app = make_app(config)
        app.run(
            host=parsed_cmd.listen,
            port=int(parsed_cmd.port),
            workers=parsed_cmd.workers,
            backlog=parsed_cmd.backlog,
            debug=parsed_cmd.debug)

    if parsed_cmd.option in ("update-db", "init-db"):
        from patton_server.dal.updater import update_db

        if parsed_cmd.option == "update-db":
            update_db(**config)
        if parsed_cmd.option == "init-db":
            config["INIT_DB"] = True
            update_db(**config)


if __name__ == '__main__':
    main()
