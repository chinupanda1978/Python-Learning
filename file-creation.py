import os
os.system("touch file2.txt")
x=os.system("test -f file2.txt")
if(x):
	print("File already exist")
else:
	print("file created succesfully") 
exit()
