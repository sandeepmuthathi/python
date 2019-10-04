import sys
import requests
import argparse
parser = argparse.ArgumentParser(description="site24x7 checker")
parser.add_argument('--host',dest='url', required=True,help='Test your URL')
args=parser.parse_args()

url=args.url
#url=sys.argv[1]

headers={'Host':'eig-wp-test-site.com' , 'User-agent':'Site24x7'}
if "Monitor Site" in requests.get('http://{}/uncached'.format(url), headers=headers).text:
    print("Site is up")
else: 
    print("Site is down, check further")
