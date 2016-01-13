
#!/usr/bin/env python

# /users/chadell/Google Drive/FORMACIO/CURS PYTHON

import re

f = open ("r1_cdp.txt")

a = f.read()

#print a

a_var = re.search(r"Device ID: (.+)",a)
print "Hostname: ",a_var.group(1)

a_var = re.search(r"IP address: (.+)",a)
print "IP address: ",a_var.group(1)

a_var = re.search(r"Platform: (.+?) (.+?),  Capabilities: (.+?) ",a)
print "Vendor: ",a_var.group(1)
print "Model: ",a_var.group(2)
print "Device_type: ",a_var.group(3)

f.close()