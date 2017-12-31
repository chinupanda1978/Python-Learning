import os
for i in ["Sashi","Chinu","Ajay","Ganesh","Dipti"]:
        V_Ret=os.system("id "+i+" 1>/dev/null 2>/dev/null")
        if V_Ret==0:
                print(i, "User is already exist")
        else:
                os.system("useradd "+i)
		os.system("echo python@123 | passwd -- stdin "+i)
	#	os.system("echo "Password is: python@123" | mail -s "U R passwd is: "+$i"+chinupanda1978@gmail.com")
                print(i, "User created successfully")
exit()

