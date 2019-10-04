count=0
with open('/home/sandeep.m/testing/test') as fh:
    for line in fh:
        lcount=line.count(" ")
        count=count+lcount
print(count)