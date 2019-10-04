import os
for i,j,k in os.walk("/home/sandeep.m/fuji/"): 
       for files in k: 
          flist=os.path.join(i,files)  
          if os.path.getsize(flist) == 0: 
             print(flist) 
