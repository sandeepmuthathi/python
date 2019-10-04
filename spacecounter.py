counter=0
with open('/home/sandeep.m/testing/test') as FH:
	for line in FH.readline():
		if line.isspace():
			counter=counter+1 
print(counter)

