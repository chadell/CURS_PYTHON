
#!/usr/bin/env python

# /users/chadell/Google Drive/FORMACIO/CURS PYTHON

import re

f = open ("ospf_single_interface.txt")

a = f.read()

a_var = re.search(r"(.+?) ",a)
print "Int: ",a_var.group(1)
a_var = re.search(r"Internet Address (.+?), Area (.+?),",a)
print "IP: ",a_var.group(1)
print "Area: ",a_var.group(2)
a_var = re.search(r"Network Type (.+?), Cost: (.+?)",a)
print "Type: ",a_var.group(1)
print "Cost: ",a_var.group(2)
a_var = re.search(r"Timer intervals configured, Hello (.+?), Dead (.+?),",a)
print "Hello: ",a_var.group(1)
print "Dead: ",a_var.group(2)

f.close()