#!/usr/bin/python
import os
V_Ip=["192.168.1.5","192.168.1.1","192.168.1.10"]
for i in V_Ip:
	V_Ret=os.system("ping -c 3 "+i+" 1>/dev/null 2>/dev/null")
	if V_Ret==0:
		print(i, "is pingable...")
	else:
		print(i, "is not pingable...")
exit()
