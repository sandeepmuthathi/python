import requests
import json
import re
api="https://api.wordpress.org/core/version-check/1.7/"                                                                                                                                                   
response=requests.get(api)
content=response.json()
current=content.get('offers')[0].get('current')
vfile='/home/sandeep.m/Downloads/wordpress/wp-includes/version.php'
with open(vfile) as fh:
    for line in fh.readlines():
        if "$wp_version =" in line:
            vers=re.findall(r'\d.+\d',line)
if current == vers[0]:
    print("You have lastest version")
else:
    print("Plesae update your wordpress")