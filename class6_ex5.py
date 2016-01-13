import class6_ex4
import class6_ex3

ip_addr = input("Please, enter a valid IP address: ")

if (class6_ex3.IP_validation(ip_addr) == True):
	
	print (class6_ex4.Convert_dec_to_bin(ip_addr))

else:
	print ("IP incorrecta")