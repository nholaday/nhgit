import datetime
import time

# You can see datetime has 3 main modules: date, time, and datetime
print(dir(datetime))

# date: year, month, day
d = datetime.date(2017, 1, 10)
# time: hour, min, sec
t = datetime.time(5, 1, 10)
# datetime combines both
dt = datetime.datetime(2017, 1, 10, 5, 1, 10)

# today's date
today = datetime.datetime.today()
print(today)

# string parsing
datestr = "7/10/1956"
print(datetime.datetime.strptime(datestr, "%m/%d/%Y"))

timenow = time.time()
print(timenow)
dtnow = datetime.datetime.now()
print(dtnow)

connow = datetime.datetime.fromtimestamp(timenow)
print("time.time() converted to datetime: {}".format(connow))
