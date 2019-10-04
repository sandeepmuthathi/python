import random
with open('sowpods.txt') as fh:
    wlist=fh.readlines()
r=random.randint(1,267750)
word=wlist[r]
print(word)