
import operator

#opens the file
file = open("read.txt")

requests = {}
totalRequests = 0
successRequests = 0
errorRequests = 0
redirectedRequests = 0

#initialize array of 12 month to store requests of each month
months = [[] for x in range(12)]

#loops through each line of file
for x in open(LOCAL_FILE).readlines():
	#splits the record by space to parse
	record = x.split()
	#print(record)
	
	#parses requests and sees what kind of request code it has and how many made
	try:
		request = record[6]
		htmlCode = record[8]
		if htmlCode[0] == "4":
			errorRequests += 1
		elif htmlCode[1] == "3":
			redirectedRequests += 1
		else:
			successRequests += 1
		if request in requests.keys():
			requests[request] += 1
		else:
			requests[request] = 1
		totalRequests += 1
	#skips requests if it is malformed
	except IndexError:
		pass
