word=input("Enter your choice of word:")
Lcount=0
Ucount=0
for i in word:
    if i.islower() is True:
        Lcount=Lcount+1
    elif i.isupper() is True:
        Ucount=Ucount+1
print("Lower letter count: {}".format(Lcount))
print("Upper letter count: {}".format(Ucount))