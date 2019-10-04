import subprocess as sp
with open('/etc/hostname') as fh:
    name=fh.readline()
log='/var/lib/mysql/{}'.format(name).rstrip('\n')+".err"
with open(log) as fh:
    for line in fh.readlines():
        if "crashed" in line:
        db=line.split('/')[4]
        sp.call('mysqlcheck -r {}',db)
        