import os
mydict={}
myfiles=[]
for RootDir, SubDir, Files in os.walk('/home/sandeep.m/test'):
    for file in Files:
        abspath=os.path.join(RootDir,file)
        inode=os.stat(abspath).st_ino
        if inode not in mydict:
            mydict[inode]=myfiles
        else:
            myfiles.append(abspath)
print(mydict)
#print(mydict.values())
#print(mydict.keys())