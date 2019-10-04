import re

#logline="Oct  8 22:00:00 dev-db crond[18340]: (root) CMD (/bin/sh /home/root/bin/system_check &)"

def cronparser(line):
    regex_time=r'(?P<time>[a-zA-Z]{3}\s.+?\s.+?\s)'
    regex_space = r'\s'
    regex_hostname=r'(?P<hostname>.+?)'
    regex_process=r'(?P<process>.+?)'
    regex_user=r'(?P<user>\(.+?\))'
    regex_command=r'(?P<command>\(.+\))'
    pattern=regex_time+regex_hostname+regex_space+regex_process+regex_user+regex_space+"CMD"+regex_space+regex_command
    r=re.match(pattern,line)
    return print(r.groupdict())

with open('/var/log/cron') as fh:
    f=fh.readlines()
    for logline in f:
        cronparser(logline)