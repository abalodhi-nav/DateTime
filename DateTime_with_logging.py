####################
#    Imports       #
####################

import os
from datetime import datetime as built_in_datetime
from datetime import date

from dateutil.relativedelta import relativedelta
import calendar
import time
import copy
from global_vars import LOG_PATH
from logprint import *


######################
# Utility functions  #
######################


def setPythonPath():
    new_path = "/home/src/components:/home/src/custom/ajb/osos/middleTier:/home/src/custom/ajb/osos/config:/home/src/custom/ajb/osos/middleTier/osos:/home/src/custom/ajb/osos/middleTier/domains:/home/src/custom/ajb/osos/selfService/src:/home/src/custom/ajb/osos/admin/src:/home/src/custom/ajb/osos/reports:/home/src/components/restful/src:/usr/lib/python2.7/dist-packages:/usr/local/lib/python2.7/dist-packages"
    if new_path not in os.environ.get(['PYTHONPATH'], '').split(os.pathsep):
        os.environ["PYTHONPATH"] = new_path + os.pathsep + os.environ.get('PYTHONPATH', '')


######################
#     constants      #
######################
oneDay = relativedelta(hours=24)  # one day = 24 hours


#######################
#      Classes        #
#######################

class osos_datetime(built_in_datetime):
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

    ##############################
    # operator overloading funcs #
    ##############################

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
        current_date = self
        year = current_date.year if year is None else int(year)
        month = current_date.month if month is None else int(month)
        day = current_date.day if day is None else int(day)
        # TODO : this doesn't take hour, minute, second yet
        replaced = current_date.replace(year=year, month=month, day=day)

        print("datetime implementation of rebuild() : " + str(replaced))

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
        day_one = built_in_datetime(1, 1, 1)  # January 1, 0001
        absdate = (now - day_one).days + 1
        abstime = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

        print("datetime implementation of absvalues() : (" + str(absdate) + " , " + str(abstime) + ")")

        return (absdate, abstime)

    def ticks(self):
        '''
        '''
        ticks_per_second = 1  # 10**3 Number of ticks in one second
        delta = self - osos_datetime(1969, 12, 31, 00, 00, 00)
        ticks = delta.total_seconds() * ticks_per_second

        print("datetime implementation of ticks() : " + str(ticks))

        return '{:.2f}'.format(ticks)


class DateTime(osos_datetime):
    '''
    DateTime class for working with dates and times.
    '''

    def __init__(self, year, month, day, hour=0, minute=0, second=0, microsecond=0):
        '''
        Constructor of DateTime using datetime
        '''
        self.datetime = osos_datetime(year, month, day, hour, minute, second, microsecond)
        self.day_of_week = self.weekday()
        self.days_in_month = calendar.monthrange(self.year, self.month)[1]

    def strftime(self, format_string):
        '''
        '''
        datetime_formatted = self.datetime.strftime(format_string)

        # AttributeError: 'module' object has no attribute 'strftime'

        print("Formatted datetime (using datetime module): " + str(datetime_formatted))

        return datetime_formatted


######################
#   more constants   #
######################
DateTimeType = type(osos_datetime.now())


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
        dtobj = osos_datetime.now()
        datetimeNow = dtobj.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
        datetimeNow = osos_datetime.strptime(datetimeNow, '%Y-%m-%d %H:%M:%S.%f')
    except Exception, e:
        mx_log_msg("METHOD: now()")
        mx_log_msg("PID: " + str(os.getpid()))
        mx_log_msg("FAILED: " + str(e) + "\n")
        raise e
    else:
        mx_log_msg("METHOD now()+ PID: " + str(os.getpid()) + "\n")

    return dtobj


def today():
    '''
    the today function of datetime vs mx.DateTime
    ###########################################
    return type :

    '''
    try:
        datetimeToday = date.today()
        dateToday = osos_datetime(datetimeToday.year, datetimeToday.month, datetimeToday.day)
    except Exception, e:
        mx_log_msg("METHOD: today()")
        mx_log_msg("PID: " + str(os.getpid()))
        mx_log_msg("FAILED: " + str(e) + "\n")
        raise e
    else:
        mx_log_msg("METHOD today() PID: " + str(os.getpid()) + "\n")

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
    parsedDT = osos_datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    print
    'datetime implementation of ParseDateTime() : ' + str(parsedDT)

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
        mx_log_msg("METHOD: Date()|" + str(year) + "|" + str(month) + "|" + str(day))
        mx_log_msg("PID: " + str(os.getpid()))
        mx_log_msg("FAILED: " + str(e))
        raise e
    else:
        mx_log_msg(
            "METHOD Date()|" + str(year) + "|" + str(month) + "|" + str(day) + " PID: " + str(os.getpid()) + "\n")
    return date


#######################
#   String <-> Time   #
#######################

def strptime(datetime_string, format_string):
    '''
    '''
    parsed_datetime = osos_datetime.strptime(datetime_string, format_string)
    print("datetime implementation of strptime() : " + str(parsed_datetime))
    return parsed_datetime


def strftime(date_object, format_string='%c'):
    '''
    '''
    datetime_formatted = osos_datetime.strftime(date_object, format_string)

    print("datetime implementation of strftime() : " + str(datetime_formatted))

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
        mx_log_msg("METHOD: RelativeDateTime()|" + str(years) + "|" + str(months) + "|" + str(weeks) + "|" + str(
            days) + "|" + str(hours) + "|" + str(minutes) + "|" + str(seconds) + " PID: " + str(
            os.getpid()) + " " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S"))
        mx_log_msg("FAILED: " + str(e) + "\n")
        raise e
    else:
        mx_log_msg("METHOD: RelativeDateTime()|" + str(years) + "|" + str(months) + "|" + str(weeks) + "|" + str(
            days) + "|" + str(hours) + "|" + str(minutes) + "|" + str(seconds) + " PID: " + str(
            os.getpid()) + " " + built_in_datetime.now().strftime("%d.%b %Y %H:%M:%S" + "\n"))

    return delta


##########################################
#     dir(mx.DateTime.now()) functions   #
##########################################


def gmtime(date=osos_datetime.utcnow(), tzone_offset_in_min=0):
    '''
    Custom gmtime() function that calculates the local time given a UTC datetime and timezone offset.

    Parameters:
        date (datetime.datetime): The UTC datetime object. Defaults to the current UTC datetime.
        tzone_offset_in_min (int): The timezone offset in minutes. Defaults to 0 (no offset).

    #########################################################################################
    Returns:
        datetime.datetime: The local datetime object based on the provided UTC datetime and timezone offset.
    '''

    gm_datetime = date + relativedelta(minutes=tzone_offset_in_min)
    print("datetime implementation of gmtime() : " + str(gm_datetime))

    return gm_datetime


def localtime(local_datetime=osos_datetime.now()):
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
        local_datetime = osos_datetime(1969, 12, 31, 19, 00, 00) + relativedelta(seconds=local_datetime)

    print("datetime implementation of localtime() : " + str(local_datetime))

    return local_datetime


####################################
#     dir(mx.DateTime) functions   #
####################################

def DateFrom(local_datetime=osos_datetime.now()):
    '''
    '''
    if isinstance(local_datetime, int):  # if ticks are given
        local_datetime = osos_datetime(1969, 12, 31, 19, 00, 00) + relativedelta(seconds=local_datetime)

    print("datetime implementation of DateFrom() : " + str(local_datetime))

    return local_datetime


def DateTimeFrom(local_datetime=osos_datetime.now()):
    '''
    '''
    if isinstance(local_datetime, int):  # if ticks are given
        local_datetime = osos_datetime(1969, 12, 31, 19, 00, 00) + relativedelta(seconds=local_datetime)

    print("datetime implementation of DateTimeFrom() : " + str(local_datetime))

    return local_datetime


def DateTimeFromTicks(local_datetime=osos_datetime.now()):
    '''
    '''
    if isinstance(local_datetime, int):  # if ticks are given
        local_datetime = osos_datetime(1969, 12, 31, 19, 00, 00) + relativedelta(seconds=local_datetime)

    print("datetime implementation of DateTimeFromTicks() : " + str(local_datetime))

    return local_datetime


###################################################
#           Relative Time Difference              #
###################################################

def RelativeDate(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):
    '''
    '''

    delta = relativedelta(years=years, months=months, weeks=weeks, days=days, hours=hours, minutes=minutes,
                          seconds=seconds, microseconds=0)

    var2 = built_in_datetime.now() + delta

    var2_str = var2.strftime("%Y-%m-%d %H:%M:%S")

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

    print("dateutil implementation of RelativeDateTimeDiff() : " + str(rel_del))

    return rel_del


def RelativeDateDiff(date1=None, date2=None):
    '''
    '''
    # Check if both dates are provided
    if date1 is None or date2 is None:
        raise ValueError("Both date1 and date2 must be provided.")

    # Calculate the difference between the two dates
    rel_del = relativedelta(date1, date2)

    print("dateutil implementation of RelativeDateDiff() : " + str(rel_del))

    return rel_del


def TimeDelta(hours=0, minutes=0, seconds=0):
    '''
    '''
    time_delta = relativedelta(hours=hours, minutes=minutes, seconds=seconds)

    print("dateutil implementation of TimeDelta() : " + str(time_delta))

    return time_delta


################################################################

def mktime(time_obj):
    '''
    makes time
     tuple has to be a 9-tuple (year,month,day,hour,minute,second,dow,doy,dst).
    '''
    time = osos_datetime(time_obj.tm_year, time_obj.tm_mon, time_obj.tm_mday, time_obj.tm_hour, time_obj.tm_min,
                         time_obj.tm_sec)
    # print("datetime implementation of mktime() : " + str(time) )

    return time


def DateTimeFromString(date_string):
    dtFromStr = osos_datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')

    print("datetime implementation of DateTimeFromString() : " + str(dtFromStr))

    return dtFromStr


def Time(hours=0, minutes=0, seconds=0):
    '''
    '''
    time_delta = relativedelta(hours=hours, minutes=minutes, seconds=seconds)

    print("dateutil implementation of Time() : " + str(time_delta))

    return time_delta


def mx_log_msg(msg):
    try:
        mx_log_filename = os.path.join('/home/abalodhi/src/', 'mx.log')
        mx_logfile = open(mx_log_filename, 'a+')
    except IOError, e:
        logprint('Error opening the logfile: %s:%s\n' % (mx_log_filename, str(e)))
        exit()
    try:
        mx_logfile.write('%s \n' % (msg))
        mx_logfile.flush()
    except IOError, e:
        logprint('Error occurred writing to logfile: %s : %s' % (mx_log_filename, str(e)))
        exit(mx_logfile)
    mx_logfile.close()



