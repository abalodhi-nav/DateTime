####################
#    Imports       #
####################

import os
from datetime import datetime as built_in_datetime
from datetime import date
import mx.DateTime
from dateutil.relativedelta import relativedelta
import calendar

######################
# Utility functions  #
######################


def setPythonPath():
    
    new_path = "/home/src/components:/home/src/custom/ajb/osos/middleTier:/home/src/custom/ajb/osos/config:/home/src/custom/ajb/osos/middleTier/osos:/home/src/custom/ajb/osos/middleTier/domains:/home/src/custom/ajb/osos/selfService/src:/home/src/custom/ajb/osos/admin/src:/home/src/custom/ajb/osos/reports:/home/src/components/restful/src:/usr/lib/python2.7/dist-packages:/usr/local/lib/python2.7/dist-packages"
    if new_path not in os.environ.get(['PYTHONPATH'], '').split(os.pathsep):
        os.environ["PYTHONPATH"] = new_path + os.pathsep + os.environ.get('PYTHONPATH','')


#######################
#      Classes        #
#######################

class datetime(built_in_datetime):
    '''
    CustomDateTime class that inherits from the built-in datetime.datetime class.
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor override to add required attributes
        '''
        built_in_datetime.__init__(self, *args, **kwargs)

        # Extra attributes
        self.day_of_week = self.weekday()
        self.days_in_month = calendar.monthrange(self.year, self.month)[1]


    def rebuild(self, year=None, month=None, day=None, hour=None, minute=None, second=None, timezone=None, r=None, dst=None):
        '''
        Rebuilds the datetime object with specified attributes.

        Args:
            year (int): The year.
            month (int): The month.
            day (int): The day.
            hour (int): The hour.
            minute (int): The minute.
            second (int): The second.
            timezone: The timezone.
            r: The r attribute.
            dst: The dst attribute.

        ###########################################
        returns:
            CustomDateTime: The rebuilt datetime object
        '''
        current_date = self  
        year = current_date.year if year is None else int(year)
        month = current_date.month if month is None else int(month)
        day = current_date.day if day is None else int(day)
        return current_date.replace(year=year, month=month, day=day)  


    def Format(self, format_string):
        '''
        ###########################################
        '''
        return self.strftime(format_string)

    def absvalues(self):
        '''
        '''
        return self.abs()



class DateTime:
    '''
    DateTime class for working with dates and times.
    '''

    def __init__ (self, year, month, day, hour=0, minute=0, second=0, microsecond=0 ):
        '''
        Constructor of DateTime using datetime
        '''
        self.datetime = built_in_datetime(year, month, day, hour, minute, second, microsecond)
        self.day_of_week = self.datetime.weekday()
        self.days_in_month = calendar.monthrange(year, month)[1]


    def __str__ (self):
        #print "Values : " + str(self.day) + "/" + str(self.month) + "/" + str(self.year) + " | " + str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)
        return self.datetime.strftime("%Y-%m-%d %H:%M:%S")


    def strftime (self, format_string):
        return self.datetime.strftime(format_string)


########################
#      functions       #
########################


def now():
    '''
    the now function of datetime vs mx.DateTime
    ###########################################
    return : 
        datetimeNow = current timestamp , object of class P3.mx.DateTime.datetime
     
    '''
    datetimeNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
    datetimeNow = datetime.strptime(datetimeNow, '%Y-%m-%d %H:%M:%S.%f')
    
    print "datetime implementation of datetime now() : " + str(datetimeNow)
    print "mx.DateTime implementation of datetime now() : " + str(mx.DateTime.now())
    
    return datetimeNow


def today(): 
    '''
    the today function of datetime vs mx.DateTime
    ###########################################
    return type :

    '''
    datetimeToday = date.today()
    dateToday = datetime(datetimeToday.year,datetimeToday.month,datetimeToday.day)    
    print "The datetime implementation is: " + str(dateToday)
    
    # TODO comment the following and return dateToday
    print "mx.DateTime  implementation of datetime today : " + str(mx.DateTime.today())
    return dateToday


def ParseDateTime(date_str):
    '''
    the ParseDateTime function of mx.DateTime
    NOTE : THis is used in files :
    aosos\custom\ajb\osos\server_agent\Resume.py
    aosos\custom\ajb\osos\server_agent\Job.py

    TODO : Verify if these files are still in use
    
    ###########################################
    return type :

    '''
    parsedDT = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    print 'datetime implementation of ParseDateTime = ' + str(parsedDT)
    
    print 'mx.DateTime implementation of ParseDateTime = '  + str(mx.DateTime.ISO.ParseDateTime(date_str))

    return parsedDT


#####################
#    Constructors   #
#####################
    
def Date(year, month, day):
    '''
    Constructor of the Date
    ###########################################
    return type :
        DateTime
    '''
    date = DateTime(year, month, day)
    print "mx.DateTime implementation of Date : " + date.__str__()
    print "datetime implementation is Date : " + str(datetime(year,month,day))
    return date


#######################
#   String <-> Time   #
#######################

def strptime(datetime_string, format_string):
    '''
    '''
    parsed_datetime = datetime.strptime(datetime_string, format_string)
    print("Parsed datetime: " + str(parsed_datetime))
    return parsed_datetime



def RelativeDateTime(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):   
    '''
    '''    

    var = mx.DateTime.now() + mx.DateTime.RelativeDateTime(years=years, months=months, weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    delta = relativedelta(years=years, months=months, weeks=weeks, days=days,  hours=hours, minutes=minutes, seconds=seconds, microseconds=0)

    var2 = built_in_datetime.now() + delta

    var_str = var.strftime("%Y-%m-%d %H:%M:%S")
    var2_str = var2.strftime("%Y-%m-%d %H:%M:%S")

    print("mx.DateTime implementation of RelativeDateTime :  " + var_str)
    print("dateutil implementation of RelativeDateTime : " + var2_str)

    return  delta

