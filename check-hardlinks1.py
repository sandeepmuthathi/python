import os

hard_dict = {}

for rootDir,subDirs,subFiles in os.walk('/bin'):
  for subFile in subFiles:
    absPath = os.path.join(rootDir,subFile)
    inode = os.stat(absPath).st_ino
    
    if inode not in hard_dict:
      hard_dict[inode] = []
      hard_dict[inode].append(absPath)
    else:
      hard_dict[inode].append(absPath)

    print(hard_dict)
    input()