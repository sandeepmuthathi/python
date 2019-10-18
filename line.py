lis1=[]
n=0
with open('/home/sandeep.m/sasasad') as fh:
    ab=fh.readlines()
    for i in range(int(100/3)):
        lis1.append([])
        for j in range(n,n+3):
            lis1[i].append(ab[j].strip('\n'))
        n=n+3
for i in range(int(100/3)):
    print(" ".join(lis1[i]))
