####################
#    Imports       #
####################

from datetime import datetime as inbuilt_datetime
from datetime import date
import os
import mx.DateTime


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

class datetime(inbuilt_datetime):
    '''
    datetime class inherits from the inbuilt datetime.datetime class
    '''
    def __init__(self, *args, **kwargs):
        '''
        override the constructor to add required attributes
        '''
        inbuilt_datetime.__init__(self, *args, **kwargs)

        # Extra attributes
        self.day_of_week = self.weekday()


    def test(self):
        print("test")


class DateTime:
    '''
    '''

    def __init__ (self, year, month, day, hour=0, minute=0, second=0, microsecond=0 ):
        '''
        Constructor of DateTime using datetime
        '''
        self.datetime = inbuilt_datetime(year, month, day, hour, minute, second, microsecond)
        self.weekday = self.datetime.weekday
        self.day_of_week = self.weekday()


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
    '''
    datetimeNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
    datetimeNow = datetime.strptime(datetimeNow, '%Y-%m-%d %H:%M:%S.%f')
    print "datetime implementation of datetime now() : " + str(datetimeNow)

    # TODO comment the following out and return the datetimeNow
    print "mx.DateTime implementation of datetime now() : " + str(mx.DateTime.now())
    return datetimeNow


def today(): 
    '''
    the today function of datetime vs mx.DateTime
    '''
    datetimeToday = inbuilt_datetime.date.today()
    # the .today() gives non-zero Time stamp in datetime, hence creating an object this way 
    dateToday = inbuilt_datetime(datetimeToday.year,datetimeToday.month,datetimeToday.day)    
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
    '''
    parsedDT = inbuilt_datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

    print 'datetime implementation of ParseDateTime = ' + str(parsedDT)

    return parsedDT


#####################
#    Constructors   #
#####################
    
def Date(year, month, day):

    date = DateTime(year, month, day)
    print "mx.DateTime implementation of Date : " + date.__str__()
    print "datetime implementation is Date : " + str(inbuilt_datetime(year,month,day))
    return date


#######################
#   String <-> Time   #
#######################

def strptime(datetime_string, format_string):
    from datetime import datetime
    return datetime.strptime(datetime_string, format_string)



def RelativeDateTime(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):   
    '''
    years=0,months=0,days=0, year=0,month=0,day=0, hours=0,minutes=0,seconds=0, hour=None,minute=None,second=None, weekday=None,weeks=0
    '''    

    from dateutil.relativedelta import relativedelta

    var = mx.DateTime.now() + mx.DateTime.RelativeDateTime(years=years, months=months, weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    delta = relativedelta(years=years, months=months, weeks=weeks, days=days,  hours=hours, minutes=minutes, seconds=seconds, microseconds=0)
    var2 = inbuilt_datetime.now() + delta


    var_str = var.strftime("%Y-%m-%d %H:%M:%S")
    var2_str = var2.strftime("%Y-%m-%d %H:%M:%S")

    print("mx.DateTime implementation of RelativeDateTime :  " + var_str)
    print("dateutil implementation of RelativeDateTime : " + var2_str)

    return  delta

