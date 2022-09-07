import time;      # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

print (time.localtime());

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

#python3 pyConcepts/date_time/time.py