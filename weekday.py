# Weekly Task for Week 05
# program that outputs whether or not today is a weekday
# Author: Gillian Kane-McLoughlin

# need to import Python's datetime module
import datetime

datetime.datetime.today()
day = datetime.datetime.today().weekday()
# Ref: https://intellipaat.com/community/5576/how-do-i-get-the-day-of-week-given-a-date-in-python

if day == 5 or day == 6: # 5 should be Saturday & 6 Sunday
    print ("It's the Weekend!")
else:
    print ("Unfortunately, today is a Weekday")