import subprocess
import re
import os

if os.path.exists("/usr/local/eig_zabbix/tmp/"):
    zabbix_data = "/usr/local/eig_zabbix/tmp/corosync.tmp"
else:
    zabbix_data = "/opt/eig_linux/data/corosync.tmp"

p=subprocess.Popen(["crm_mon","-1"], stdout = subprocess.PIPE)
OutString=p.communicate()
on_nodes=len(re.search(r'Online: \[(.*)?\]',str(OutString)).group(1).split())
c_nodes=re.search(r'(\d)\s?nodes\sconfigured',str(OutString)).group(1)
c_resources=re.search(r'(\d)\s?resources\sconfigured',str(OutString)).group(1)
s_resources=str(s).count('Started')

with open(zabbix_data, 'w') as data:

if int(c_nodes) == int(on_nodes):
    with open(zabbix_data, 'w') as data:
        data.write("corosync_nodes 0\n")
else:
    with open(zabbix_data, 'w') as data:
        data.write("corosync_nodes 1\n")

if s_resources == int(c_resources):
    with open(zabbix_data, 'a') as data:
        data.write("resources 0")
else:
    with open(zabbix_data, 'a') as data:
        data.write("resources 1\n")  