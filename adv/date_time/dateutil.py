# python3 adv/date_time/dateutil.py


from dateutil import parser

date_time = parser.parse("Mar 11 2011 11:31AM")

print(date_time)
print(type(date_time))