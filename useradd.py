#!/bin/python
import os
for i in ["sashi","chinu","dipti"]:
	V_Ret=os.system("id "+i+" 1>/dev/null 2>/dev/null")
	if V_Ret==0:
		print(i, "User is already exist...")
	else:
		os.system("useradd "+i)

		print(i, "User created successfully...")
exit()
