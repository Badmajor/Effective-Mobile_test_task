import argparse
import sys

from constants import DOCS, COMMANDS
from utils import Wallet


def add_subparsers(parser: argparse.ArgumentParser):
    """Добавляет команды с аргументами в parser."""
    subparsers = parser.add_subparsers()
    for cmd, settings in COMMANDS.items():
        parser = subparsers.add_parser(
            cmd,
            help=settings['help']
        )
        for field, description in settings['fields'].items():
            parser.add_argument(
                f'-{field[0]}',
                f'--{field}',
                help=description,
                required=settings['required']
            )
        if settings['cursor']:
            parser.add_argument(
                '-f',
                '--field',
                help='Поле которое нужно поменять',
                required=True
            )
            parser.add_argument(
                '-n',
                '--new',
                help='Новое значение',
                required=True
            )


def main(argv: list):
    wallet = Wallet()
    parser = argparse.ArgumentParser(description=DOCS)
    add_subparsers(parser)
    if len(argv) == 0:
        parser.print_help()
        sys.exit(1)
    args: argparse.Namespace = parser.parse_args()
    cmd = argv[0]
    run = getattr(wallet, cmd)
    run(args)


if __name__ == '__main__':
    main(sys.argv[1:])
