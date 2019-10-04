SrcFile=open("/home/sandeep.m/python/while.py", "r")
Contents=SrcFile.read()
DstFile=open("/home/sandeep.m/python/while.py.back", "w")
DstFile.write(Contents)
SrcFile.close
DstFile.close