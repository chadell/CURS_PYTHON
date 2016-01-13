
#!/usr/bin/env python

# /users/chadell/Google Drive/FORMACIO/CURS PYTHON

import re

f = open ("sw1_cdp.txt")

a = f.read()

device_id = re.findall(r"Device ID: (.+)",a)

print device_id

ip_address = re.findall(r"IP address: (.+)",a)

print ip_address

platform = re.findall(r"Platform: (.+?),",a)

print platform

f.close()
