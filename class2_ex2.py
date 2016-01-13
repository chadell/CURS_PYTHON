a = input("Please, enter an IP network: ")
b = a.split(".")
first_octet = b[0]
second_octet = b[1]
third_octet = b[2]
fourth_octet = b[3]

print ("%-20s%-20s%-20s%-20s" % ("first_octet","second_octet","third_octet","fourth_octet"))
print ("%-20s%-20s%-20s%-20s" % (bin(int(first_octet)),bin(int(second_octet)),bin(int(third_octet)), bin(int(fourth_octet))))

#tinc algun \n que es cola entre prints