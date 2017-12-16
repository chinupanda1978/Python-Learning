import os
x=os.system("rpm -q httpd* 1>output.txt")
if(x):
	print("Package Not available")
else:
	print("Package alredy exist") 
exit()
