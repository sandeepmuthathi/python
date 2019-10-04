import re
ip=input()
pattern=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
match=re.match(pattern,ip)
if match:
    print("yes, that is an IP")
else: 
    print("invalid IP")