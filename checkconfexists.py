import os
with open('/home/sandeep.m/python/config.txt') as FH:
    for conf in FH.readlines():
        if os.path.isfile(conf.rstrip('\n')):
            print('{} : Exists'.format(conf.rstrip('\n')))
        else:
            print('{} : Does not exist'.format(conf.rstrip('\n')))
