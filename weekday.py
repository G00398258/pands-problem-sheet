# Weekly Task for Week 05
# program that outputs whether or not today is a weekday
# Author: Gillian Kane-McLoughlin

# See README file for references
# need to import Python's datetime module
import datetime

datetime.datetime.today()
day = datetime.datetime.today().weekday()

if day == 5 or day == 6: # 5 should be Saturday & 6 Sunday
    print ("It's the Weekend!")
else:
    print ("Unfortunately, today is a Weekday")