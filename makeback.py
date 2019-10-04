import os
import sys
file=sys.argv[1]
type(file)
#print(file)
os.system('cp {} {}.back'.format(file, file))

