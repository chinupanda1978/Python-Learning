#!/bin/pytho
import os
V_Package=input("Provide a package name: ")
V_Ret=os.system("rpm -qa "+V_Package+" 1>/dev/null 2>/dev/null")
if V_Ret==0:
	print("Package is Installed...")
else:
	V_Ret1=os.system("yum list all | grep "+V_Package +" 1>/dev/null 2>/dev/null")
	if (V_Ret1==0):
		os.system("yum install -y "+V_Package)
	print("Package is not available in reposerver...")
