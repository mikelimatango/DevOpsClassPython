from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'read.txt'

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z:
print('.', end=", flush=True))
      
import operator

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

print("\nREQUEST COUNTS:")
requests = sorted(requests.items(), key=operator.itemgetter(1))


print("totalRequests:",totalRequests)
print("Percentage of unsuccessful requests:","{0:.2}%".format((errorRequests)/(errorRequests + redirectedRequests + successRequests)*100))
print("Percentage of redirected requests:","{0:.2}%".format((redirectedRequests)/(errorRequests + redirectedRequests + successRequests)*100))
print("Least requested:", requests[0])
print("Most requested:", requests[-1])
