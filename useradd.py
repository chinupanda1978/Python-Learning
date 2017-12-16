import os
x=os.system("useradd Chinu 1>output.txt 2>error.txt")
if(x):
	print("User Chinu  already exist")
else:
	print("user Chinu created successfully")
exit()
