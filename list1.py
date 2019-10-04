#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the 'merge_lists' function below.

def merge_lists():
    L1=[]
    L2=[]
    n1=input("enter the number of elements in L1: ")
    n2=input("enter the number of elements in L2: ")
    for i in range(1,int(n1)+1):
        item=input()
        L1.append(item)
    for i in range(1,int(n2)+1):
        item1=input()
        L2.append(item1)
    L4=L1+L2
    L3=sorted(L4)
    print(L3)
    return(print(L3))

if __name__ == '__main__':
    merge_lists()

