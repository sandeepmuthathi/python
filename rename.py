import os
for file in os.listdir('/home/sandeep.m/testing'):
    path=os.path.join('/home/sandeep.m/testing',file)
    if path.endswith('txt'):
        rfile=path.split('.txt')
        os.rename(path,"{}.html".format(path))
    

