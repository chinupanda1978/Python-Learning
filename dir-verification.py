import os
os.system("mkdir dir2 1>output.txt 2>error.txt")
x=os.system("test -d dir2")
if(x):
      print("Directory already exist")
else:
     print("Directory created successfully")
exit()
