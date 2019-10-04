import os
mydict={}
myfiles=[]
for RootDir, SubDir, Files in os.walk('/home/sandeep.m/test'):
    for file in Files:
        
        abspath=os.path.join(RootDir,file)
        inode=os.stat(abspath).st_ino
        #if myfiles=[]
        if os.stat(abspath).st_nlink > 1:
            mydict[inode]=myfiles
         #  myfiles.append(abspath)
print(mydict)
#print(mydict.values())
#print(mydict.keys())
