import re
mail = input("your email:")
print mail
r1 = re.compile(r'\w+\@gmail\.com')
#print r1
mat = r1.match(mail)
if mat: 
	print " yes, email"
else:
	print "not email"

