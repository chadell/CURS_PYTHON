def convert_list_to_dictionary (a_list):
	a ={}
	for i in a_list:
		a[i]=""
	return a

	
list = ["item1","item2","item3"]	
print (list)
dict = convert_list_to_dictionary (list)
print (dict)