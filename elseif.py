N = int(input())

if N%2 != 0:
    print("Weird")
elif N in range(2,5):
    print("Not Weird")
elif N in range(6,20):
    print("Weird")
elif N > 20:
    print("Not Weird")
