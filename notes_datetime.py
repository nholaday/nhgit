import datetime
import pytz

#######################Date########################
d = datetime.date(2017, 7, 6)
print d

# Today
tday = datetime.date.today()
print(tday)
print(tday.weekday()) # Monday 0, Sunday 6

# Time Delta
tdelta = datetime.timedelta(days=7)
print("One week from now {}".format(tday + tdelta))
print("Subtracting a date from another date results in a timedelta {}".format(tday - d))
print((tday - d).days)

##################Time################
t = datetime.time(9, 30, 45, 100000) # Hour, min, sec, microsec
print("datetime.time {}, just the hour {}".format(t, t.hour))

#################Datetime###############
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)
print("Date {} Time {} individually".format(dt.date(), dt.time()))
print("Year {}".format(dt.year))

# Dealing with timezones (Timezone aware)
# pip install pytz
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
print("Current time with UTC offset {}".format(dt))
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print("Current UTC time {}".format(dt_utcnow))

dt_pst = dt_utcnow.astimezone(pytz.timezone('US/Pacific'))
print("Current Pacific time {}".format(dt_pst))

# Converting dates to strings with strftime
print(dt_pst.strftime('%B %d, %Y')) # look up strftime tables online

# Converting strings to dates with strptime
date_string = "October/16/2010"
dt2 = datetime.datetime.strptime(date_string, "%B/%d/%Y")
print(dt2)
