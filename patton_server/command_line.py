import logging
import argparse
import os.path as op

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

    # --------------------------------------------------------------------------
    # Parser: update
    # --------------------------------------------------------------------------
    init_db = subparsers.add_parser('init-db', help='create and populate DB')

    update = subparsers.add_parser('update-db', help='update CVE & CPE info')
    update.add_argument(
        '-W', '--web-hook',
        dest="WEB_HOOK",
        help='url to notify new loaded CVEs',
        default=None
    )

    # TODO
    # backup = subparsers.add_parser('backup',
    #                                help='create a backup of database data')
    # backup.add_argument(
    #     '-f', '--dump-file',
    #     dest="DUMP_FILE",
    #     help='file name to store the results. Must be .sql',
    #     default=False
    # )

    return parser.parse_args()


def main():

    parsed_cmd = argument_parser()

    # set logger level
    log_level = abs(50 - ((parsed_cmd.LOG_LEVEL * 10) % 50))
    log.setLevel(log_level)

    #
    # Run actions
    #
    if parsed_cmd.option == "serve":
        from patton_server import make_app

        here = op.abspath(op.dirname(__file__))

        app = make_app(op.join(here, "config.py"))
        app.run(
            host=parsed_cmd.listen,
            port=parsed_cmd.port,
            workers=parsed_cmd.workers,
            backlog=parsed_cmd.backlog,
            debug=parsed_cmd.debug)

    if parsed_cmd.option in ("update-db", "init-db"):
        from patton_server import update_db, load_config_from_pyfile

        # Get general config
        config = load_config_from_pyfile(
            op.join(op.dirname(__file__), "config.py")
        )

        # Overwrite with command line options
        config.update(dict(parsed_cmd._get_kwargs()))

        if parsed_cmd.option == "update-db":
            update_db(**config)
        if parsed_cmd.option == "init-db":
            config["INIT_DB"] = True
            update_db(**config)


if __name__ == '__main__':
    main()
