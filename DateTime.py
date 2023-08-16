####################
#    Imports       #
####################

import os
from datetime import datetime as built_in_datetime
from datetime import date
import mx.DateTime
from dateutil.relativedelta import relativedelta
import calendar
import time
import copy

######################
# Utility functions  #
######################


def setPythonPath():
    
    new_path = "/home/src/components:/home/src/custom/ajb/osos/middleTier:/home/src/custom/ajb/osos/config:/home/src/custom/ajb/osos/middleTier/osos:/home/src/custom/ajb/osos/middleTier/domains:/home/src/custom/ajb/osos/selfService/src:/home/src/custom/ajb/osos/admin/src:/home/src/custom/ajb/osos/reports:/home/src/components/restful/src:/usr/lib/python2.7/dist-packages:/usr/local/lib/python2.7/dist-packages"
    if new_path not in os.environ.get(['PYTHONPATH'], '').split(os.pathsep):
        os.environ["PYTHONPATH"] = new_path + os.pathsep + os.environ.get('PYTHONPATH','')


######################
#     constants      #
######################
oneDay =  relativedelta(hours=24)  # one day = 24 hours


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
        self.oneDay =  relativedelta(hours=24)

    def rebuild(self, year=None, month=None, day=None, hour=None, minute=None, second=None, timezone=None):
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

        ###########################################
        returns:
            CustomDateTime: The rebuilt datetime object
        '''
        current_date = self  
        year = current_date.year if year is None else int(year)
        month = current_date.month if month is None else int(month)
        day = current_date.day if day is None else int(day)
        # TODO : this doesn't take hour, minute, second yet        
        replaced = current_date.replace(year=year, month=month, day=day)

        print ("datetime implementation of rebuild() : " + str(replaced) )
        print ("mx.DateTime implementation of rebuild() : " + str(mx.DateTime.now().rebuild(year=year, month=month, day=day) ))

        return replaced


    def Format(self, format_string):
        '''
        ###########################################
        '''
        return self.strftime(format_string)

    def absvalues(self):
        '''
        ###########################################
        '''
        now = self
        day_one = datetime(1, 1, 1) # January 1, 0001
        absdate = (now - day_one).days + 1 
        abstime = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        
        print ("datetime implementation of absvalues() : (" + str(absdate) + " , "+ str(abstime) +")")
        print ("mx.DateTime implementation of absvalues() : " + str(mx.DateTime.now().absvalues()))
        
        return (absdate, abstime)

    

class DateTime(datetime):
    '''
    DateTime class for working with dates and times.
    '''

    def __init__ (self, year, month, day, hour=0, minute=0, second=0, microsecond=0 ):
        '''
        Constructor of DateTime using datetime
        '''
        self.datetime = datetime(year, month, day, hour, minute, second, microsecond)
        self.day_of_week = self.weekday()
        self.days_in_month = calendar.monthrange(self.year, self.month)[1]

    def strftime(self, format_string):
        '''
        '''
        datetime_formatted = self.datetime.strftime(format_string)

        #mx_datetime_formatted = mx.DateTime.strftime(self.datetime, format_string)
        # AttributeError: 'module' object has no attribute 'strftime'
 
        print("Formatted datetime (using datetime module): " + str(datetime_formatted))
        #print("Formatted datetime (using mx.DateTime module): " + str(mx_datetime_formatted))
        
        return datetime_formatted


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
    
    print "datetime implementation of now() : " + str(datetimeNow)
    print "mx.DateTime implementation of now() : " + str(mx.DateTime.now())
    
    return datetimeNow


def today(): 
    '''
    the today function of datetime vs mx.DateTime
    ###########################################
    return type :

    '''
    datetimeToday = date.today()
    dateToday = datetime(datetimeToday.year,datetimeToday.month,datetimeToday.day)    
    
    print "datetime implementation of today() : " + str(dateToday)
    print "mx.DateTime implementation of today() : " + str(mx.DateTime.today())
    
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
    print 'datetime implementation of ParseDateTime() : ' + str(parsedDT)
    
    print 'mx.DateTime implementation of ParseDateTime() : '  + str(mx.DateTime.ISO.ParseDateTime(date_str))

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
    print "mx.DateTime implementation of constructor Date() : " + date.__str__()
    print "datetime implementation is constructor Date() : " + str(datetime(year,month,day))
    return date


#######################
#   String <-> Time   #
#######################

def strptime(datetime_string, format_string):
    '''
    '''
    parsed_datetime = datetime.strptime(datetime_string, format_string)
    print("datetime implementation of strptime() : " + str(parsed_datetime))
    # print("time parsed as per mx.DateTime: " + str(mx.DateTime.strftime(mx.DateTime.strptime(datetime_string, format_string), format_string  ))
    return parsed_datetime


def strftime(date_object, format_string='%c'):
    '''
    '''
    datetime_formatted = datetime.strftime(date_object, format_string)
    # mx_datetime = mx.DateTime.DateTimeFromTicks(date_object)
    # mx_datetime_formatted = mx.DateTime.strftime(date_object, format_string)

    print("datetime implementation of strftime() : " + str(datetime_formatted))
    #print("Formatted datetime (using mx.DateTime module): " + str(mx_datetime_formatted))

    return datetime_formatted


########################
#      time delta      #
########################

def RelativeDateTime(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):   
    '''
    '''    

    var = mx.DateTime.now() + mx.DateTime.RelativeDateTime(years=years, months=months, weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    delta = relativedelta(years=years, months=months, weeks=weeks, days=days,  hours=hours, minutes=minutes, seconds=seconds, microseconds=0)

    var2 = built_in_datetime.now() + delta

    var_str = var.strftime("%Y-%m-%d %H:%M:%S")
    var2_str = var2.strftime("%Y-%m-%d %H:%M:%S")

    print("mx.DateTime implementation of RelativeDateTime() :  " + var_str)
    print("dateutil implementation of RelativeDateTime() : " + var2_str)

    return delta


##########################################
#     dir(mx.DateTime.now()) functions   #
##########################################


def gmtime(date=datetime.utcnow(), tzone_offset_in_min=0):
    '''
    Custom gmtime() function that calculates the local time given a UTC datetime and timezone offset.

    Parameters:
        date (datetime.datetime): The UTC datetime object. Defaults to the current UTC datetime.
        tzone_offset_in_min (int): The timezone offset in minutes. Defaults to 0 (no offset).

    #########################################################################################
    Returns:
        datetime.datetime: The local datetime object based on the provided UTC datetime and timezone offset.
    '''
    
    gm_datetime = date  + relativedelta(minutes=tzone_offset_in_min) 
    print("mx.DateTime implementation of gmtime() :  " + str(mx.DateTime.gmtime() + mx.DateTime.TimeDelta(minutes=tzone_offset_in_min)))
    print("datetime implementation of gmtime() : " + str(gm_datetime) )

    return gm_datetime



def localtime(local_datetime=datetime.now()):
    '''
    Converts a given local datetime object or ticks to a modified local datetime object.

    Args:
        local_datetime (datetime.datetime or int, optional): The local datetime object or ticks.
            If not provided, the current datetime is used. 
            If an integer is provided, it is treated as ticks.

    ################################################################################
    Returns:
        datetime.datetime: The modified local datetime object.

    '''

    if isinstance(local_datetime, int):
        print("mx.DateTime implementation of localtime() :  " + str(mx.DateTime.localtime(local_datetime) ))
        local_datetime = datetime(1969,12, 31, 19,00,00) + relativedelta(seconds=local_datetime)
    else:
        print("mx.DateTime implementation of localtime() :  " + str(mx.DateTime.localtime() )) #TODO put localtime here which returns datetime


    print("datetime implementation of localtime() : " + str(local_datetime) )

    return local_datetime


####################################
#     dir(mx.DateTime) functions   #
####################################

def DateFrom(local_datetime=datetime.now()):
    '''
    '''
    if isinstance(local_datetime, int): # if ticks are given
        print("mx.DateTime implementation of DateFrom() :  " + str(mx.DateTime.DateFrom(local_datetime) ))
        local_datetime = datetime(1969,12, 31, 19,00,00) + relativedelta(seconds=local_datetime)
    else:
        print("mx.DateTime implementation of DateFrom() :  " + str(mx.DateTime.DateFrom(local_datetime) ))

    print("datetime implementation of DateFrom() : " + str(local_datetime) )

    return local_datetime


def DateTimeFrom(local_datetime=datetime.now()):
    '''
    '''
    if isinstance(local_datetime, int): # if ticks are given
        print("mx.DateTime implementation of DateTimeFrom() :  " + str(mx.DateTime.DateTimeFrom(local_datetime) ))
        local_datetime = datetime(1969,12, 31, 19,00,00) + relativedelta(seconds=local_datetime)
    else:
        print("mx.DateTime implementation of DateTimeFrom() :  " + str(mx.DateTime.DateTimeFrom(local_datetime) ))

    print("datetime implementation of DateTimeFrom() : " + str(local_datetime) )

    return local_datetime


def DateTimeFromTicks(local_datetime=datetime.now()):
    '''
    '''
    if isinstance(local_datetime, int): # if ticks are given
        print("mx.DateTime implementation of DateTimeFromTicks() :  " + str(mx.DateTime.DateTimeFromTicks(local_datetime) ))
        local_datetime = datetime(1969,12, 31, 19,00,00) + relativedelta(seconds=local_datetime)
    else:
        print("mx.DateTime implementation of DateTimeFromTicks() :  " + str(mx.DateTime.DateTimeFromTicks() ))

    print("datetime implementation of DateTimeFromTicks() : " + str(local_datetime) )

    return local_datetime


###################################################
#           Relative Time Difference              #
###################################################

def RelativeDate(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):
    '''
    '''

    var = mx.DateTime.now() + mx.DateTime.RelativeDate(years=years, months=months, weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    delta = relativedelta(years=years, months=months, weeks=weeks, days=days,  hours=hours, minutes=minutes, seconds=seconds, microseconds=0)

    var2 = built_in_datetime.now() + delta

    var_str = var.strftime("%Y-%m-%d %H:%M:%S")
    var2_str = var2.strftime("%Y-%m-%d %H:%M:%S")

    print("mx.DateTime implementation of RelativeDate() :  " + var_str)
    print("dateutil implementation of RelativeDate() : " + var2_str)

    return delta


def RelativeDateTimeDiff(date1=None, date2=None):
    '''
    '''
    # Check if both dates are provided
    if date1 is None or date2 is None:
        raise ValueError("Both date1 and date2 must be provided.")
    
    # Calculate the difference between the two dates
    rel_del = relativedelta(date1, date2)
   
    print("mx.DateTime implementation of RelativeDateTimeDiff() :  " + str(mx.DateTime.RelativeDateTimeDiff(mx.DateTime.DateTime(date1.year, date1.month, date1.day, date1.hour, date1.minute, date1.second), (mx.DateTime.DateTime(date2.year, date2.month, date2.day, date2.hour, date2.minute, date2.second)) )))
    print("dateutil implementation of RelativeDateTimeDiff() : " + str(rel_del) )

    return rel_del

def RelativeDateDiff(date1=None, date2=None):
    '''
    '''
    # Check if both dates are provided
    if date1 is None or date2 is None:
        raise ValueError("Both date1 and date2 must be provided.")

    # Calculate the difference between the two dates
    rel_del = relativedelta(date1, date2)

    print("mx.DateTime implementation of RelativeDateDiff() :  " + str(mx.DateTime.RelativeDateTimeDiff(mx.DateTime.DateTime(date1.year, date1.month, date1.day, date1.hour, date1.minute, date1.second), (mx.DateTime.DateTime(date2.year, date2.month, date2.day, date2.hour, date2.minute, date2.second)) )))
    print("dateutil implementation of RelativeDateDiff() : " + str(rel_del) )

    return rel_del




def TimeDelta(hours=0,minutes=0,seconds=0):
    '''
    '''
    tim_del = mx.DateTime.TimeDelta(hours=hours, minutes=minutes, seconds=seconds)
    time_delta = relativedelta( hours=hours, minutes=minutes, seconds=seconds)
    
    print("mx.DateTime implementation of TimeDelta() :  " + str(tim_del) )
    print("dateutil implementation of TimeDelta() : " + str(time_delta) )

    return time_delta
