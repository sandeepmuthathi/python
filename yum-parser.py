import re

logline="Oct  8 22:00:00 dev-db crond[18340]: (root) CMD (/bin/sh /home/root/bin/system_check &)"


def parsecron(line):
    regex_time=r'(?P<time>[a-zA-Z]{3}\s.+?\s.+?\s)'
    regex_space = r'\s'
    regex_hostname=r'(?P<hostname>.+?)'
    regex_process=r'(?P<process>.+?:)'
    regex_user=r'(?P<user>\(.+?\))'
    regex_command=r'(?P<command>\(.+\)'
    pattern=regex_time+regex_space+regex_hostname+regex_space+regex_user+regex_process+regex_space+CMD+regex_space+regex_command
    r=re.match(pattern,line)
    r.groupdict()


parsecron(logline)


def parser(line):
  regex_host = r'(?P<host>.+?)' 
  regex_space = r'\s'
  regex_identity = r'(?P<identity>.+?)'
  regex_user = r'(?P<user>.+?)'
  regex_time = r'(?P<time>\[.+?\])'
  regex_request = r'(?P<request>\".+?\")'
  regex_status = r'(?P<status>\d{3})'
  regex_size = r'(?P<size>.+?)' 
  regex_referer = r'(?P<referer>\".+?\")' 
  regex_agent = r'(?P<agent>\".+?\")'

  pattern = regex_host+regex_space+regex_identity+regex_space+regex_user+regex_space+ \
            regex_time+regex_space+regex_request+regex_space+regex_status+regex_space+ \
            regex_size+regex_space+regex_referer+regex_space+regex_agent

  r = re.match(pattern,logLine)
  return r.groupdict()
l
ogLine = '180.76.15.30 - - [24/Mar/2017:19:37:57 +0000] "GET /shop/page/32/?count=15&orderby=title&add_to_wishlist=4846 HTTP/1.1" 404 10202 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"'
In [142]:

  Oct  8 22:00:00 dev-db crond[18340]: (root) CMD (/bin/sh /home/root/bin/system_check &)
