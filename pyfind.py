import argparse
import os

parser=argparse.ArgumentParser(description="Search files usingit's extentions")
parser.add_argument('-l', dest='home',required=True, help='location')
parser.add_argument('-t', dest='ext',required=True, help='extention')
args=parser.parse_args()

for RootDir, SubDir, Files in os.walk(args.home):
    for file in Files:
        if file.endswith('.{}'.format(args.ext)):
            print(os.path.join(RootDir,file))
