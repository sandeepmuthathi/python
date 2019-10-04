from datetime import date
import subprocess as sp
x=date.today()
sp.call('touch file-{}.txt'.format(x),shell=True)

