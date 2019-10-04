names={}
with open('/home/sandeep.m/maintanance.txt') as fh:
    for i in fh.readlines():
        i=i.strip()
        if i in names.keys():
            names[i]=names.get(i)+1
        else:
            names[i]=1
print(names)