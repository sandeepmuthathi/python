import time
def function():
    total=0
    for num in range(5000000):
        total=total+num
    return total

start=time.process_time()
result=function()
exectime=time.process_time()-start
print(exectime)