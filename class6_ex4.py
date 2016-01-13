
def Convert_dec_to_bin(ip_addr):

	import sys

	#ip_addr = sys.argv.pop()
	#print (ip_addr)

	b = ip_addr.split(".")

	for i,element in enumerate (b):
		b[i] = bin (int(element))
		
	a = ["0","0","0","0"]
	c = ["0","0","0","0"]

	for j in range(len(b)):
		a[j] = b[j][2:]
		a[j] = "00000000" + a[j] 
		c[j] = a[j][-8:]
		
	#print ("%-20s%-20s" % ("IP address","Binary"))
	#print ("%-20s%-20s" % (ip_addr,".".join(c)))
	
	return ".".join(c)