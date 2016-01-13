#!/usr/bin/env python

# /users/chadell/GoogleDrive/FORMACIO/CURS_PYTHON
#import sys
#sys.path.append("path/to/Modules")

def IP_validation(ip_addr):
	
	ip_bona = False
	octets = ip_addr.split('.')	

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

if __name__ == '__main__':
	test_ip_addresses = {
	        '192.168.1' : False,
	        '10.1.1.' : False,
	        '10.1.1.x' : False,
	        '0.77.22.19' : False,
	        '-1.88.99.17' : False,
	        '241.17.17.9' : False,
	        '127.0.0.1' : False,
	        '169.254.1.9' : False,
	        '192.256.7.7' : False,
	        '192.168.-1.7' : False,
	        '10.1.1.256' : False,
	        '1.1.1.1' : True,
	        '223.255.255.255': True,
	        '223.0.0.0' : True,
	        '10.200.255.1' : True,
	        '192.168.17.1' : True,
	}
	print "Executing test code"
	for k,v in test_ip_addresses.items():
		if ((IP_validation(k)) != v):
			print "The function doesn't work properly, concretely with",k
	



