import os
fileSizeDict = {}

for f in os.listdir('/home/sandeep.m'):
    absPath = os.path.join('/home/sandeep.m',f)
    if absPath.endswith('.conf'):
        size = os.path.getsize(absPath)
        fileSizeDict[absPath] = size
#print(fileSizeDict)

def getSize(t):
    return t[1]

sorted(fileSizeDict.items(),key=getSize)[::-1][:5] 