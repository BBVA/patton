import argparse
from .profiling import profile_ctx


def argument_parser():
    parser = argparse.ArgumentParser(
        description='Retrieve stdin and analyze it for vulnerabilities'
    )

    parser.add_argument(
        '-s', '--separator', help='Configure separator for packer version tuples: default " "',
        type=str,
        default=' ',
    )

    parser.add_argument(
        '-r', '--recreate', help='Wipe current db and recreate the schema',
        action='store_true',
        default=False
    )

    parser.add_argument(
        '-u', '--update', help='Update the DB',
        action='store_true',
    )

    parser.add_argument(
        '-p', '--profile', help='Dump profile execution to the given PROFILE path',
        type=str,
        default='',
    )

    return parser.parse_args()


def main():
    args = argument_parser()

    with profile_ctx(args.profile):
        print(args)

        if args.recreate:
            from .dal.database import recreate
            recreate()

            # INFO: this needs to be after recreating the DB in order to avoid circular import errors
            from .dal.loader import cpe_loader, cve_loader
            cpe_loader()
            cve_loader()


if __name__ == '__main__':
    main()
