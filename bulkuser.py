import os
fp=open("userlist.txt")
for V_Line in fp.readlines():
	V_List=V_Line.split("\n")
	V_User=V_List[0]
	V_Ret=os.system("id "+V_User+" 1>/dev/null 2>/dev/null")
        if V_Ret==0:
                print(V_User, "User is already exist")
        else:
                os.system("useradd "+V_User)
		os.system("echo python@123 | passwd --stdin "+V_User)
                print(V_User, "User created successfully")	
