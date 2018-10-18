
import operator

#opens the file
file = open("read.txt")

requests = {}
totalRequests = 0
successRequests = 0
errorRequests = 0
redirectedRequests = 0

months = [[] for x in range(12)]

for x in file.readlines():
	record = x.split()
	print(record, end="")
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
	except IndexError:
		pass
