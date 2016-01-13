#C:\Users\HP\AppData\Local\Programs\Python\Python35-32

import sys


ip_addr = sys.argv.pop()

#print (ip_addr)

b = ip_addr.split(".")

for i,element in enumerate (b):
	b[i] = bin (int(element))
	

#print ("%-20s%-20s%-20s%-20s" % (b[0],b[1],b[2],b[3]))

a = ["0","0","0","0"]
c = ["0","0","0","0"]

for j in range(len(b)):
	a[j] = b[j][2:]
	#print (a[j])
	
	a[j] = "00000000" + a[j] 
	
	c[j] = a[j][-8:]
	#print (c[j])
	
print ("%-20s%-20s" % ("IP address","Binary"))
print ("%-20s%-20s" % (ip_addr,".".join(c)))
	
		
