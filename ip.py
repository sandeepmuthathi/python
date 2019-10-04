import sys
import ipaddress 
ip=sys.argv[1]
#check_ip(ip) 

def check_ip(x):
	if ipaddress.ip_address(x):
		return print('Its an IP')
try:
	check_ip(ip)
except ValueError: 
	print("not an IP")
finally: 
	print("Thank you")
