import os
import argparse
parser=argparse.ArgumentParser(description='Find Env Variables')
parser.add_argument('-v',dest="var", required=True, help="give var name")
args=parser.parse_args()
print(os.environ[args.var])