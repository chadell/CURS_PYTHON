entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24     157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24    157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

entry_list = entry1.split(" ")
ip_prefix = entry_list [2]
a = entry1.split(" 0 ")
b = a[1]
c = b.split(" ")
as_path = c [:-1]
print ("%-20s%-20s" % ("IP_PREFIX","AS_PATH"))
print ("%-20s%-20s" % (ip_prefix,as_path))

entry_list = entry2.split(" ")
ip_prefix = entry_list [2]
a = entry2.split(" 0 ")
b = a[1]
c = b.split(" ")
as_path = c [:-1]
print ("%-20s%-20s" % ("IP_PREFIX","AS_PATH"))
print ("%-20s%-20s" % (ip_prefix,as_path))

entry_list = entry3.split(" ")
ip_prefix = entry_list [2]
a = entry3.split(" 0 ")
b = a[1]
c = b.split(" ")
as_path = c [:-1]
print ("%-20s%-20s" % ("IP_PREFIX","AS_PATH"))
print ("%-20s%-20s" % (ip_prefix,as_path))

entry_list = entry4.split(" ")
ip_prefix = entry_list [2]
a = entry4.split(" 0 ")
b = a[1]
c = b.split(" ")
as_path = c [:-1]
print ("%-20s%-20s" % ("IP_PREFIX","AS_PATH"))
print ("%-20s%-20s" % (ip_prefix,as_path))

