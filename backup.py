import os
import sys
import shutil

File=sys.argv[1]
#FileName = os.path.basename(File)
#BaseDir = os.path.dirname(File)
BackupFile = '{}.backup'.format(File)
shutil.copyfile(File,BackupFile)
