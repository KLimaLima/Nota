import argparse

import cli.basic as basic

parser = argparse.ArgumentParser(
    prog="nota",
    description="Note taking CLI for Nota",
    epilog="Thanks for using %(prog)s! :)")

basic_subparser = parser.add_subparsers(
    title="basic",
    dest="name",
    help="the basic utilities"
)

# arg_template = {
    # "dest": "operands",
    # "type": str,
    # "nargs": 2,
    # "metavar": "OPERAND",
    # "help": "a numeric value",
# }
dest = "operands"

# change this from "new" to "empty"
new_parser = basic_subparser.add_parser("new", help="creates a new md file")
# greet_parser.add_argument(**arg_template)
new_parser.add_argument(dest=dest, nargs=1)
new_parser.set_defaults(func=basic.create_md)

baru_parser = basic_subparser.add_parser("baru", help="creates a new md file")
baru_parser.add_argument(dest=dest, nargs=1)
baru_parser.set_defaults(func=basic.create_md)

create_parser = basic_subparser.add_parser("create", help="converts html to stylised webpage")
create_parser.add_argument(dest=dest, nargs=1)
create_parser.set_defaults(func=basic.create_nota)

args = parser.parse_args()
args.func(*args.operands)

# uv run -m cli new <filename>