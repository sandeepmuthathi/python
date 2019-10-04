import os
import sys
import subprocess as sp
File=sys.argv[1]
FileName = os.path.basename(File)
BaseDir = os.path.dirname(File)
BackupFile = os.path.join(BaseDir,'{}.backup'.format(FileName))
#print(BackupFile)
#sp.call('cp {} {}'.format(FileName, BackupFile), shell=True)
sp.call('cp FileName BackupFile')
