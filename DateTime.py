####################
#    Imports       #
####################

import os
from datetime import datetime as built_in_datetime
from datetime import date
from datetime import timedelta

from dateutil.relativedelta import relativedelta
import calendar
import time
import copy
from global_vars import LOG_PATH
from logprint import *


######################
#     constants      #
######################
oneDay = relativedelta(hours=24)  # one day = 24 hours


#######################
#      Classes        #
#######################

class ososDelta(timedelta):
    def absvalues(self):
        days = self.days
        seconds = self.seconds
        return (days,seconds)
    

class DateTime(built_in_datetime):
    '''
    A custom datetime class that inherits from the built-in datetime.datetime class.
    '''
    
    def __init__(self, *args, **kwargs):
        '''
        Constructor override to add required attributes
        '''
        built_in_datetime.__init__(self, *args, **kwargs)

        # Extra attributes
        self.day_of_week = self.weekday()
        self.days_in_month = calendar.monthrange(self.year, self.month)[1]
        self.oneDay = relativedelta(hours=24)
        #the '+1' us kludge to make it work exactly as  original mx.DateTime
        self.absdate = (self - built_in_datetime(1, 1, 1, 0, 0)).days +1
        datetimeToday = date.today()
        dateToday = built_in_datetime(datetimeToday.year, datetimeToday.month, datetimeToday.day, 0, 0, 0)
        self.abstime = float((self-dateToday).seconds)
        if self.year >= 1900:
            self.formatted_date = self.strftime("%Y-%m-%d")

    ##############################
    # operator overloading funcs #
    ##############################
    def get_date(self):
        return self.formatted_date

    def __sub__(self, other):
        if type(other) in [int,float]:
            try:
                return built_in_datetime.__sub__(self,timedelta(days=other))
            except Exception, e:
                mx_log_msg("METHOD: DateTime subtraction operator for integers")
                mx_log_msg("PID: "+str(os.getpid()))
                mx_log_msg("FAILED: " +str(e))
                raise e
            else:
                mx_log_msg("METHOD: DateTime subtraction operator for integers\n")
        time_delta_obj = built_in_datetime.__sub__(self,other)
        if type(other) == DateTime:
            #convert so we can get absvalues. Don't need cast logic here.
            return ososDelta(time_delta_obj.days,time_delta_obj.seconds,time_delta_obj.microseconds)
        return time_delta_obj
        

    def __add__(self, other):
        if type(other) in [int,float]:
            try:
                return built_in_datetime.__add__(self,timedelta(days=other))
            except Exception, e:
                mx_log_msg("METHOD: DateTime addition operator for integers")
                mx_log_msg("PID: "+str(os.getpid()))
                mx_log_msg("FAILED: " +str(e))
                raise e
            else:
                mx_log_msg("METHOD: DateTime addition operator for integers\n")
        value = built_in_datetime.__add__(self,other)
        if type(value) == built_in_datetime:
            value = DateTime(value.year,value.month,value.day,value.hour,value.minute,value.second)
        return value

    def __lt__(self, arg):
        '''
        Override the less than (<) operator .
        #########################################
        Args:
            arg: The object to compare with.
        ###########################################
        Returns:
            bool: True if the CustomDateTime object is less than the given object, False otherwise.
        '''
        if arg is None:
            return False
        return built_in_datetime.__lt__(self, arg)

    def __le__(self, arg):
        '''
        Override the less than equals to (<=) operator .
        #######################################
        Args:
            arg: The object to compare with.
        #######################################
        Returns:
            bool: True if the CustomDateTime object is less than equal to the given object, False otherwise.
        '''
        if arg is None:
            return False
        return built_in_datetime.__le__(self, arg)

    def __eq__(self, arg):
        '''
        Override the equals (==) operator .
        ##########################################
        Args:
            arg: The object to compare with.
        ##########################################
        Returns:
            bool: True if the CustomDateTime object is equal the given object, False otherwise.
        '''
        if arg is None:
            return False
        return built_in_datetime.__eq__(self, arg)

    def __ne__(self, arg):
        '''
        Override the not equals (!=) operator .
        ######################################
        Args:
            arg: The object to compare with.
        ####################################
        Returns:
            bool: True if the CustomDateTime object is less than the given object, False otherwise.
        '''
        if arg is None:
            return True
        return built_in_datetime.__ne__(self, arg)

    def __ge__(self, arg):
        '''
        Override the greater than equals to (>=) operator .
        ######################################################
        Args:
            arg: The object to compare with.
        ############################################
        Returns:
            bool: True if the CustomDateTime object is greater than equal to the given object, False otherwise.
        '''
        if arg is None:
            return False
        return built_in_datetime.__ge__(self, arg)

    def __gt__(self, arg):
        '''
        Override the greater than (>) operator .
        #########################################
        Args:
            arg: The object to compare with.
        ####################################
        Returns:
            bool: True if the CustomDateTime object is greater than the given object, False otherwise.
        '''
        if arg is None:
            return False
        #The following block is when we don't whant to check if an object is an int, float or DateTime in the application code.
        #A bit of a kludge that the orignal mx.DateTime supports.  Very seldom used.
        if type(arg) == int or type(arg) == float:
            if self.year > arg:
                return True
            return False
        return built_in_datetime.__gt__(self, arg)

    ###################################
    #   functions not in built_in_dt  #
    ###################################
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
        try :
            current_date = self
            year = current_date.year if year is None else int(year)
            month = current_date.month if month is None else int(month)
            day = current_date.day if day is None else int(day)
            hour = current_date.hour if hour is None else int(hour)
            minute = current_date.minute if minute is None else int(minute)
            second = current_date.second if second is None else int(second)
            replaced = current_date.replace(year=year, month=month, day=day, hour=hour, minute=minute, second=second)


        except Exception, e:
            mx_log_msg("METHOD: DateTimerebuild()|"+str(year)+"|"+str(month)+"|"+str(day)+"|"+str(hour)+"|"+str(minute)+"|"+str(second)+"|"+str(timezone))
            mx_log_msg("PID: "+str(os.getpid()))
            mx_log_msg("FAILED: " +str(e))
            raise e
        else:
            mx_log_msg("METHOD DateTime.rebuild()|"+str(year)+"|"+str(month)+"|"+str(day)+"|"+str(hour)+"|"+str(minute)+"|"+str(second)+"|"+str(timezone)+ " PID: "+str(os.getpid())+"\n")

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
        try :
            now = self
            day_one = built_in_datetime(1, 1, 1)  # January 1, 0001
            absdate = (now - day_one).days + 1
            abstime = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

        except Exception, e:
            mx_log_msg("METHOD: DateTime.absvalues()|"+str(self))
            mx_log_msg("PID: "+str(os.getpid()))
            mx_log_msg("FAILED: " +str(e))
            raise e
        else:
            mx_log_msg("METHOD DateTime.absvalues()|"+str(self)+ " PID: "+str(os.getpid())+"\n")

        return (absdate, abstime)

    def ticks(self):
        '''
        '''
        try :
            ticks_per_second = 1  # 10**3 Number of ticks in one second
            delta = self - DateTime(1969, 12, 31, 00, 00, 00)
            ticks = delta.total_seconds() * ticks_per_second

        except Exception, e:
            mx_log_msg("METHOD: DateTime.ticks()|"+str(self))
            mx_log_msg("PID: "+str(os.getpid()))
            mx_log_msg("FAILED: " +str(e))
            raise e
        else:
            mx_log_msg("METHOD DateTime.ticks()|"+str(self)+ " PID: "+str(os.getpid())+"\n")

        return ticks

    date = property(get_date)


######################
#   more constants   #
######################
DateTimeType = type(DateTime.now())


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
    try:
        dtobj = DateTime.now()
    except Exception, e:
        mx_log_msg("METHOD: now()")
        mx_log_msg("PID: "+str(os.getpid()))
        mx_log_msg("FAILED: " +str(e) +"\n")
        raise e
        
    else:
        mx_log_msg("METHOD now()+ PID: "+str(os.getpid())+"\n")


    return dtobj


def today(hour=0, min=0, sec=0):
    '''
    the today function of datetime vs mx.DateTime
    ###########################################
    return type :

    '''
    try:
        datetimeToday = date.today()
        dateToday = DateTime(datetimeToday.year, datetimeToday.month, datetimeToday.day, hour, min, sec)
    except Exception, e:
        mx_log_msg("METHOD: today()")
        mx_log_msg("PID: "+str(os.getpid()))
        mx_log_msg("FAILED: " +str(e) +"\n")
        raise e
    else:
        mx_log_msg("METHOD today() PID: "+str(os.getpid())+"\n")

    return dateToday


def ParseDateTime(date_str):
    '''
    the ParseDateTime function of mx.DateTime
    NOTE : THis is used in files 
    aosos\custom\ajb\osos\server_agent\Resume.py
    aosos\custom\ajb\osos\server_agent\Job.py

    TODO : Verify if these files are still in use

    ###########################################
    return type :

    '''
    try :
        parsedDT = DateTime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        
    except Exception, e:
        mx_log_msg("METHOD: ParseDateTime()|" + date_str)
        mx_log_msg("PID: " + str(os.getpid()) )
        mx_log_msg("FAILED: " +str(e) +"\n")
        raise e
    else:
        mx_log_msg("METHOD ParseDateTime()|" + date_str + " PID: "+str(os.getpid())+"\n")
        
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
    try:
        date = DateTime(year, month, day)
    except Exception, e:
        mx_log_msg("METHOD: Date()|"+str(year)+"|"+str(month)+"|"+str(day))
        mx_log_msg("PID: "+str(os.getpid()))
        mx_log_msg("FAILED: " +str(e))
        raise e
    else:
        mx_log_msg("METHOD Date()|"+str(year)+"|"+str(month)+"|"+str(day)+ " PID: "+str(os.getpid())+"\n")
    return date


#######################
#   String <-> Time   #
#######################

def strptime(datetime_string, format_string):
    '''
    '''
    try :
        parsed_datetime = DateTime.strptime(datetime_string, format_string)
    except Exception, e:
        mx_log_msg("METHOD: strptime()|"+datetime_string+"|"+format_string)
        mx_log_msg("PID: "+str(os.getpid()))
        mx_log_msg("FAILED: " +str(e))
        raise e
    else:
        mx_log_msg("METHOD strptime()|"+datetime_string+"|"+format_string+ " PID: "+str(os.getpid())+"\n")
    
    return parsed_datetime


def strftime(date_object, format_string='%c'):
    '''
    '''
    try :
        datetime_formatted = DateTime.strftime(date_object, format_string)
        
    except Exception, e:
        mx_log_msg("METHOD: strftime()|"+str(date_object)+"|"+format_string)
        mx_log_msg("PID: "+str(os.getpid()))
        mx_log_msg("FAILED: " +str(e))
        raise e
    else:
        mx_log_msg("METHOD strftime()|"+str(date_object)+"|"+format_string+ " PID: "+str(os.getpid())+"\n")
    
    return datetime_formatted


########################
#      time delta      #
########################

def RelativeDateTime(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):
    '''
    '''
    try:
        delta = relativedelta(years=years, months=months, weeks=weeks, days=days, hours=hours, minutes=minutes,
                          seconds=seconds, microseconds=0)
    except Exception, e:
        mx_log_msg("METHOD: RelativeDateTime()|"+str(years)+"|"+str(months)+"|"+str(weeks)+"|"+str(days)+"|"+str(hours)+"|"+str(minutes)+"|"+str(seconds)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " +str(e)+"\n")
        raise e
    else:
        mx_log_msg("METHOD: RelativeDateTime()|"+str(years)+"|"+str(months)+"|"+str(weeks)+"|"+str(days)+"|"+str(hours)+"|"+str(minutes)+"|"+str(seconds)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"+"\n"))
    
    return delta


##########################################
#     dir(mx.DateTime.now()) functions   #
##########################################

def gmtime(seconds_from_epoch=time.time()):
    '''Returns the DateTime object that is epoch + seconds_from_epoch'''
    epoch = DateTime(1970, 1, 1, 0, 0)
    return epoch + RelativeDateTime(seconds=seconds_from_epoch)
 
    
    
def gmtime2(date=DateTime.utcnow(), tzone_offset_in_min=0):
    '''
    Custom gmtime() function that calculates the local time given a UTC datetime and timezone offset.

    Parameters:
        date (datetime.datetime): The UTC datetime object. Defaults to the current UTC datetime.
        tzone_offset_in_min (int): The timezone offset in minutes. Defaults to 0 (no offset).

    #########################################################################################
    Returns:
        datetime.datetime: The local datetime object based on the provided UTC datetime and timezone offset.
    '''

    try:
        gm_datetime = date + relativedelta(minutes=tzone_offset_in_min)
    except Exception, e:
        mx_log_msg("METHOD: gmtime()|"+str(date)+"|"+str(tzone_offset_in_min)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " +str(e)+"\n")
        raise e
    else:
        mx_log_msg("METHOD: gmtime()|"+str(date)+"|"+str(tzone_offset_in_min)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"+"\n"))
    
    return gm_datetime


def localtime(local_datetime=DateTime.now()):
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
    try:
        if isinstance(local_datetime, int):
            local_datetime = DateTime(1969, 12, 31, 19, 00, 00) + relativedelta(seconds=local_datetime)
    except Exception, e:
        mx_log_msg("METHOD: localtime()|"+str(local_datetime)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " +str(e)+"\n")
        raise e
    else:
        mx_log_msg("METHOD: localtime()|"+str(local_datetime)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"+"\n"))


    return local_datetime


####################################
#     dir(mx.DateTime) functions   #
####################################

def DateFrom(local_datetime=DateTime.now()):
    '''
    '''
    try:
        if isinstance(local_datetime, int):  # if ticks are given
            local_datetime = DateTime(1969, 12, 31, 19, 00, 00) + relativedelta(seconds=local_datetime)
    except Exception, e:
        mx_log_msg("METHOD: DateFrom()|"+str(local_datetime)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " +str(e)+"\n")
        raise e
    else:
        mx_log_msg("METHOD: DateFrom()|"+str(local_datetime)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"+"\n"))

    return local_datetime


def DateTimeFrom(local_datetime=DateTime.now()):
    '''
    '''
    try :
        if isinstance(local_datetime, int):  # if ticks are given
            local_datetime = DateTime(1969, 12, 31, 19, 00, 00) + relativedelta(seconds=local_datetime)
    
    except Exception, e:
        mx_log_msg("METHOD: DateTimeFrom()|"+str(local_datetime)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " +str(e)+"\n")
        raise e
    else:
        mx_log_msg("METHOD: DateTimeFrom()|"+str(local_datetime)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"+"\n"))

    return local_datetime


def DateTimeFromTicks(local_datetime=DateTime.now()):
    '''
    '''
    try :
        if isinstance(local_datetime, int):  # if ticks are given
            local_datetime = DateTime(1969, 12, 31, 19, 00, 00) + relativedelta(seconds=local_datetime)
    
    except Exception, e:
        mx_log_msg("METHOD: DateTimeFromTicks()|"+str(local_datetime)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " +str(e)+"\n")
        raise e
    else:
        mx_log_msg("METHOD: DateTimeFromTicks()|"+str(local_datetime)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"+"\n"))

    return local_datetime


###################################################
#           Relative Time Difference              #
###################################################

def RelativeDate(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):
    '''
    '''
    try :
        delta = relativedelta(years=years, months=months, weeks=weeks, days=days, hours=hours, minutes=minutes,
                              seconds=seconds, microseconds=0)
        var2 = built_in_datetime.now() + delta
        var2_str = var2.strftime("%Y-%m-%d %H:%M:%S")
    
    except Exception, e:
        mx_log_msg("METHOD: RelativeDate()|"+str(years)+"|"+str(months)+"|"+str(weeks)+"|"+str(days)+"|"+str(hours)+"|"+str(minutes)+"|"+str(seconds)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " +str(e)+"\n")
        raise e
    else:
        mx_log_msg("METHOD: RelativeDate()|"+str(years)+"|"+str(months)+"|"+str(weeks)+"|"+str(days)+"|"+str(hours)+"|"+str(minutes)+"|"+str(seconds)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"+"\n"))


    return delta


def RelativeDateTimeDiff(date1=None, date2=None):
    '''
    '''
    try :
        # Check if both dates are provided
        if date1 is None or date2 is None:
            raise ValueError("Both date1 and date2 must be provided.")

        # Calculate the difference between the two dates
        rel_del = relativedelta(date1, date2)

    except Exception, e:
        mx_log_msg("METHOD: RelativeDateTimeDiff()|"+str(date1)+"|"+str(date2)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " +str(e)+"\n")
        raise e
    else:
        mx_log_msg("METHOD: RelativeDateTimeDiff()|"+str(date1)+"|"+str(date2)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"+"\n"))
    
    return rel_del


def RelativeDateDiff(date1=None, date2=None):
    '''
    '''
    try :
        # Check if both dates are provided
        if date1 is None or date2 is None:
            raise ValueError("Both date1 and date2 must be provided.")

        # Calculate the difference between the two dates
        rel_del = relativedelta(date1, date2)

    except Exception, e:
        mx_log_msg("METHOD: RelativeDateDiff()|"+str(date1)+"|"+str(date2)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " +str(e)+"\n")
        raise e
    else:
        mx_log_msg("METHOD: RelativeDateDiff()|"+str(date1)+"|"+str(date2)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"+"\n"))

    return rel_del


def TimeDelta(hours=0, minutes=0, seconds=0):
    '''
    '''
    try :
        time_delta = relativedelta(hours=hours, minutes=minutes, seconds=seconds)

    except Exception, e:
        mx_log_msg("METHOD: TimeDelta()|"+str(hours)+"|"+str(minutes)+"|"+str(seconds)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " +str(e)+"\n")
        raise e
    else:
        mx_log_msg("METHOD: TimeDelta()|"+str(hours)+"|"+str(minutes)+"|"+str(seconds)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"+"\n"))

    return time_delta


################################################################

def mktime(time_obj):
    '''
    makes time
     tuple has to be a 9-tuple (year,month,day,hour,minute,second,dow,doy,dst).
    '''
    try :
        time = DateTime(time_obj.tm_year, time_obj.tm_mon, time_obj.tm_mday, time_obj.tm_hour, time_obj.tm_min,
                         time_obj.tm_sec)
    except Exception, e:
        mx_log_msg("METHOD: mktime()|"+str(time_obj)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " +str(e)+"\n")
        raise e
    else:
        mx_log_msg("METHOD: mktime()|"+str(time_obj)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"+"\n"))

    return time


def DateTimeFromString(date_string):
    try:
        dtFromStr = DateTime.strptime(date_string, '%m/%d/%Y')
   
    except Exception, e:
        mx_log_msg("METHOD: DateTimeFromString()|"+date_string+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " +str(e)+"\n")
        raise e
    else:
        mx_log_msg("METHOD: DateTimeFromString()|"+date_string+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"+"\n"))

    return dtFromStr


def Time(hours=0, minutes=0, seconds=0):
    '''
    '''
    try :
        time_delta = relativedelta(hours=hours, minutes=minutes, seconds=seconds)

    except Exception, e:
        mx_log_msg("METHOD: Time()|"+str(hours)+"|"+str(minutes)+"|"+str(seconds)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " +str(e)+"\n")
        raise e
    else:
        mx_log_msg("METHOD: Time()|"+str(hours)+"|"+str(minutes)+"|"+str(seconds)+" PID: "+str(os.getpid())+" " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"+"\n"))

    return time_delta

def DateTimeFromAbsDateTime(absdate=0, abstime=0, calendar='Greogorian'):
    '''
    '''
    # Note : DateTime doesn't take year as 0 and spits out an error no matter what we do
    dt_time = DateTime(1,12,31,0,0,0) + relativedelta(year=-1) + relativedelta(days=abstime, seconds=abstime)
    return dt_time

############################
#     Logging functions    #
############################

def mx_log_msg(msg):

    try:
        mx_log_filename = os.path.join(LOG_PATH, 'mx.log')
        mx_logfile = open(mx_log_filename, 'a+')
    except IOError, e:
        logprint('Error opening the logfile: %s:%s\n' % (mx_log_filename, str(e)))
    try:
        mx_logfile.write('%s \n' % (msg))
        mx_logfile.flush()
    except IOError, e:
        logprint('Error occurred writing to logfile: %s : %s' % (mx_log_filename, str(e)))
    except Exception, e:
        pass
    try:
        mx_logfile.close()
    except Exception, e:
        pass


