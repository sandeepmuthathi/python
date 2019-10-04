l1=[]
l2=[]
n1=input("enter the number of elements in l1: ")
n2=input("enter the number of elements in l2: ")

for i in range(1,int(n1)+1):
    item=input()
    l1.append(item)

for i in range(1,int(n2)+1):
    item=input()
    l2.append(item)


def merge_lists(L1,L2):
    L3=L1+L2
    L3.sort()
    return(print(L3))

merge_lists(l1,l2)

