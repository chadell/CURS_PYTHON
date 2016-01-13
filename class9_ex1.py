
#!/usr/bin/env python

# /users/chadell/Google Drive/FORMACIO/CURS PYTHON

class IPAddress(object):
	def __init__( self,ip_addr):
		self.ip_addr = ip_addr

	def display_in_binary(self):
		a = self.ip_addr.split('.')
		return bin(int(a[0])) + '.' + bin(int(a[1])) + '.' + bin(int(a[2])) + '.' + bin(int(a[3]))
	def display_in_hex(self):
		a = self.ip_addr.split('.')
		return hex(int(a[0])) + '.' + hex (int(a[1])) + '.' + hex (int(a[2])) + '.' + hex (int(a[3]))
	def IP_validation(self):	
		ip_bona = False
		octets = self.ip_addr.split('.')	
		for i, octet in enumerate (octets):
			try:
				octets[i] = int(octet)
			except ValueError:
	            # couldn't convert octet to an integer
				return False
		if (len(octets) == 4):
			if (int(octets[0]) >= 1 and int(octets[0]) <= 223):
				if (int(octets[0]) != 127):
					if (int(octets[0]) != 169 or int(octets[1]) != 254):
						ip_bona = True
						for i in range (len(octets) - 1):
							if (octets[i+1]=='' ):
								ip_bona = False
							else:
								if(int(octets[i+1]) < 0 or int(octets[i+1]) >255):
									ip_bona = False
		return ip_bona

class IPAddressWithNetmask(IPAddress):
	def __init__(self,ip_addr_net):
		a = ip_addr_net.split('/')
		print a[0]
		print a[1]
		self.netmask = a[1]
		IPAddress.__init__(self,a[0])

ip = IPAddress('192.168.1.1')

#print ip.ip_addr
#print ip.display_in_binary()
#print ip.display_in_hex()
#print ip.IP_validation()

ip_net = IPAddressWithNetmask('10.1.1.2/24')

print ip_net.ip_addr
print ip_net.netmask

