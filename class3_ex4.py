#C:\Users\HP\AppData\Local\Programs\Python\Python35-32

import sys

ip_addr = sys.argv.pop()



ip_addr = ip_addr.split(".")

#print (ip_addr)

ip_bona = False

if (len(ip_addr) == 4):
	if (int(ip_addr[0]) >= 1 and int(ip_addr[0]) <= 223):
		if (int(ip_addr[0]) != 127):
			if (int(ip_addr[0]) != 169 or int(ip_addr[1]) != 254):
				ip_bona = True
				for i in range (len(ip_addr) - 1):
					if (int(ip_addr[i+1]) < 0 or int(ip_addr[i+1]) >255):
						ip_bona = False

if (ip_bona == True):
	print ("L'adreça IP és la: %s i és vàlida" % (".".join(ip_addr)))
else:
	print ("L'adreça IP és la: %s i és incorrecta" % (".".join(ip_addr)))