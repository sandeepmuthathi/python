i=0
fw=open('/home/sandeep.m/dclean.txt','w')
with open('/home/sandeep.m/dclean') as fh:
    contents = [ x.strip('\n') for x in fh.readlines()]
    fw.write(contents[0::2])
print(fw)