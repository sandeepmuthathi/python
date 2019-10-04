import os
for i,j,k in os.walk('/home/sandeep.m/test'):
    for files in k:
        file=os.path.join(i,files)
        if os.path.islink(file) and not os.path.exists(file):
            #print ('{}' " : is a link file".format(file))
            #orig=os.readlink(file)
            #abpath=os.path.join(i,orig)
            #if os.path.exists(abpath) != 1:
            print('{}' " is a brocken link".format(file))