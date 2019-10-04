counter=0
with open('/home/sandeep.m/maintanance.txt') as fh: 
#    lines=fh.readlines()
#print(len(lines))
    for line in fh:
        counter=counter+1
print('No of lines: {}'.format(counter))
