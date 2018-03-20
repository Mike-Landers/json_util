import argparse
from json_util import JsonUtil

parser = argparse.ArgumentParser()
parser.add_argument("--json")
args = parser.parse_args()
JsonUtil.print_terminal_kv_pairs(JsonUtil.get_terminal_kv_pairs(args.json))
