file=open("/etc/passwd", "r")
for line in file:
    a=line.split(":")
    if line.endswith('/bin/bash\n'):
        print('{} : {}'.format(a[0], a[6])) 
file.close()
    
