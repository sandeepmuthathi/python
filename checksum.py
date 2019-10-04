import hashlib
ChkSum=open('/home/sandeep.m/output.txt', 'w')
Config=open('/home/sandeep.m/python/config.txt')
for conf in Config.readlines():
    with open(conf.rstrip('\n'),'rb') as FH:
        md5=hashlib.md5(FH.read()).hexdigest()
        ChkSum.write('{:18} : {}\n'.format(conf.rstrip('\n'),md5))
ChkSum.close
Config.close

