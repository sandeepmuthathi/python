import requests
import json
import sys

mac=sys.argv[1]
response=requests.get('https://macvendors.co/api/{}/json'.format(mac))
content=response.json()
company=(content['result']['company'])
country=(content['result']['country'])

print('Company: {}'.format(company))
print('Country: {}'.format(country))