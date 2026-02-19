import argparse

import cli.basic as basic

parser = argparse.ArgumentParser()

parser.add_argument("name")
parser.add_argument("age")

args = parser.parse_args()

print(basic.greet(args.name, args.age))

# uv run -m cli <name> <age>