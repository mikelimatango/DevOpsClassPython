import operator
from urllib.request import urlretrieve
from datetime import datetime
from dateutil import parser
import ssl

#Makes sure ssl requests can be made
ssl._create_default_https_context = ssl._create_unverified_context

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'read.txt'

#retrieves URL and saves it to local file
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z:
print('.', end=", flush=True))
      

#dictionary of requests and number of times requested
requests = {}
#dictionary of dates
dates = {}

#initializes all the variables
totalRequests = 0
successRequests = 0
errorRequests = 0
redirectedRequests = 0

#initializes array of 12 month to store requests of each month
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

print("\nREQUEST COUNTS:")
#sorts the dictionary, sorts the request by number of times requested
requests = sorted(requests.items(), key=operator.itemgetter(1))

#prints answers to questions
print("Total Requests:",totalRequests)
print("Percentage of unsuccessful requests:","{0:.2}%".format((errorRequests)/(errorRequests + redirectedRequests + successRequests)*100))
print("Percentage of redirected requests:","{0:.2}%".format((redirectedRequests)/(errorRequests + redirectedRequests + successRequests)*100))
print("Least requested:", requests[0])
print("Most requested:", requests[-1])
