import time;      # This is required to include time module.
import calendar;

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

print (time.localtime());

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

cal = calendar.month(2022, 9)
print ("Here is the calendar:")
print (cal)

# python3 adv/date_time/time.py