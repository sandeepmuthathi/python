import sys
import subprocess as sub
dir=sys.argv[1]
sub.call('du -sch {}'.format(dir),shell=True)

