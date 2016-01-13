a = input("Please, enter an IP network: ")
b = a.split(".")

c = b[0:3]
c.append("0")
d = ".".join(c)

print (a)
print (b)
print (c)
print (d)
print("\n")

first_octet = int(c[0])

first_octet_bin = bin(first_octet)
first_octet_hex = hex(first_octet)

print ("%-20s%-20s%-20s" % ("NETWORK_NUMBER","FIRST_OCTET_BINARY","FIRST_OCTET_HEX"))
print ("%-20s%-20s%-20s" % (d,first_octet_bin,first_octet_hex))

#C:\Users\HP\AppData\Local\Programs\Python\Python35-32