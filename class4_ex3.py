import sys

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

uptime_list = [uptime1,uptime2,uptime3,uptime4]
uptimes = []

i = 0
for uptime in uptime_list:
	time = uptime.split(" uptime is ")
	uptimes.append({"name":time[0],"time":0})
	time_list = time[1].split(", ")
	for j,e in enumerate(time_list):
		try:
			aux = e.split(" ")
			if "year" in aux[1]:
				uptimes[i]["time"] += int(aux[0]) * 31536000
			if "week" in aux[1]:
				uptimes[i]["time"] += int(aux[0]) * 604800
			if "day" in aux[1]:
				uptimes[i]["time"] += int(aux[0]) * 86400
			if "hour" in aux[1]:
				uptimes[i]["time"] += int(aux[0]) * 3600
			if "minutes" in aux[1]:
				uptimes[i]["time"] += int(aux[0]) * 60			
		except ValueError:
			print ("Problema amb la conversió d'enter")
	i += 1


saveout = sys.stdout                                     
fsock = open('out.log', 'w')                             
sys.stdout = fsock                                       
print (uptimes) 
sys.stdout = saveout                                     
fsock.close()                                            

		
	
	

