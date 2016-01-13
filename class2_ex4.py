cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

list = cisco_ios.split(", ")

ios_version = list[2]

print (ios_version)