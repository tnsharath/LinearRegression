import datetime

def findDay(date):
	return datetime.datetime.strptime(date, "%m/%d/%Y").weekday()
	
date = "05/23/2019"
print(findDay(date))