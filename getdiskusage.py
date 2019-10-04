#Find the 5 large files in a directory:
import sys
import os
import itertools
dir=sys.argv[1]
dict={}

for Rootdir, SubDir, File in os.walk(dir):
    for file in File:
        flist=os.path.join(Rootdir,file)
        dict[flist]=os.path.getsize(flist)
sorted_d=sorted((value,key) for (key,value) in dict.items())
sorted_a=sorted(sorted_d,reverse=True)
topten=itertools.islice(sorted_a,5)
finallist=list(topten)
for key,value in finallist:
    print('{} :: {}'.format(key,value))


    