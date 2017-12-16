#!/bin/python
import os
V_User=input("Enter user name ")
V_Ret=os.system("id "+V_User+" 1>/dev/null 2>/dev/null")
if V_Ret==0:
	print(V_User+ " " "user already  exit...")
else:
        V_ret1=os.system("useradd "+V_User+" 1>/dev/null") 
        print(V_User+ " " "User created successfully...")
exit()
