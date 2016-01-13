import sys

show_ip_int_brief = '''
Interface       IP-Address  OK? Method  Status  Protocol
FastEthernet0   unassigned  YES unset   up      up
FastEthernet1   unassigned  YES unset   up      up
FastEthernet2   unassigned  YES unset   down    down
FastEthernet3   unassigned  YES unset   up      up
FastEthernet4   6.9.4.10    YES NVRAM   up      up
NVI0            6.9.4.10    YES unset   up      up
Tunnel1         16.25.253.2 YES NVRAM   up      down
Tunnel2         16.25.253.6 YES NVRAM   up      down
Vlan1           unassigned  YES NVRAM   down    down
Vlan10          10.220.88.1 YES NVRAM   up      up
Vlan20          192.168.0.1 YES NVRAM   down    down
Vlan100         10.220.84.1 YES NVRAM   up      up
'''

list_ip_int_brief = show_ip_int_brief.split("\n")

list_tuple_par = []
list_tuple = []

for i,element in enumerate(list_ip_int_brief):
	#print (element)
	a = element.split(" ")
	#print (a)
	for j,el2 in enumerate(a):
		#print (el2)
		if el2 != "" :
			list_tuple_par.append(el2)
	#print (list_tuple_par)
#print (list_tuple_par)
k = 0
for i in range (int(len(list_tuple_par)/6)) :
	#print (i)
	#print (list_tuple_par [i*6+4])
	#print (list_tuple_par [i*6+5])
	if (list_tuple_par [(i-k)*6+4] == "down") or (list_tuple_par [(i-k)*6+5] == "down") :
		#print ("entro al bucle")
		list_tuple_par.pop((i-k)*6)
		list_tuple_par.pop((i-k)*6+1)	
		list_tuple_par.pop((i-k)*6+2)
		list_tuple_par.pop((i-k)*6+3)
		list_tuple_par.pop((i-k)*6+4)
		list_tuple_par.pop((i-k)*6+5)
		k += 1
		
#print (list_tuple_par)

tuple = ()

for i in range (int(len(list_tuple_par)/6)) :
	if i != 0:
		tuple = (list_tuple_par[i*6],list_tuple_par[i*6+1],list_tuple_par[i*6+4],list_tuple_par[i*6+5])
		list_tuple.append(tuple)

#print (list_tuple)

saveout = sys.stdout
fsock = open('out_classe3_ex3.log', 'w')
sys.stdout = fsock
print (list_tuple) 
sys.stdout = saveout