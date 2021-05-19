import calendar
import datetime
import time
#print(calendar.weekhead(4))

#print(calendar.firstweekday()) #first weekday number-->0

#print(calendar.month(2020,9))  #prints the respective month's calendar.  

#print(calendar.calendar(2020))

'''mon-->0
   tue-->1
   wed-->2
   thur-->3
   fri-->4
   sat-->5
   sun-->6 '''

#day_of_the_week=calendar.weekday(2020,9,12)   #gives day 
#print(day_of_the_week)


#is_leap=calendar.isleap(2020)
#print(is_leap)


'''today=datetime.date.today()    #To see present date
print(today)
#To see present time
current_time=datetime.datetime.now()
print(current_time.day)
print(current_time.hour)
print(current_time.minute)'''

given_date=datetime.date(2019,9,12)
print(given_date)



