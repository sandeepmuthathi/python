import parser
with open('/home/sandeep.m/python/access.log') as fh: 
    for line in fh:
		log = parser.parser(line)
		#print(log)
		print(log['host']) 
