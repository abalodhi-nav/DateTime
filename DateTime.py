####################
#    Imports       #
####################

import datetime
import os
import mx.DateTime


######################
# Utility functions  #
######################


def setPythonPath():
    
    new_path = "/home/src/components:/home/src/custom/ajb/osos/middleTier:/home/src/custom/ajb/osos/config:/home/src/custom/ajb/osos/middleTier/osos:/home/src/custom/ajb/osos/middleTier/domains:/home/src/custom/ajb/osos/selfService/src:/home/src/custom/ajb/osos/admin/src:/home/src/custom/ajb/osos/reports:/home/src/components/restful/src:/usr/lib/python2.7/dist-packages:/usr/local/lib/python2.7/dist-packages"
    if new_path not in os.environ.get(['PYTHONPATH'], '').split(os.pathsep):
        os.environ["PYTHONPATH"] = new_path + os.pathsep + os.environ.get('PYTHONPATH','')


########################
#      functions       #
########################


def now():
    '''
    the now function of datetime vs mx.DateTime
    '''
    datetimeNow = datetime.datetime.now()
    print "datetime implementation of datetime now() : " + str(datetimeNow)

    # TODO comment the following out and return the datetimeNow
    print "mx.DateTime implementation of datetime now() : " + str(mx.DateTime.now())
    return datetimeNow



def today(): 
    '''
    the today function of datetime vs mx.DateTime
    '''
    datetimeToday =datetime.date.today()
    # the .today() gives non-zero Time stamp in datetime, hence creating an object this way 
    dateToday= datetime.datetime(datetimeToday.year,datetimeToday.month,datetimeToday.day)    
    print "The datetime implementation is: " + str(dateToday)
    
    # TODO comment the following and reurn dateToday
    print "mx.DateTime  implementation of datetime today : " + str(mx.DateTime.today())
    return dateToday



#####################
#    Constructors   #
#####################

class DateTime:
    '''
    '''
    def __init__ (self, year, month, day, hour=0, minute=0, second=0, microsecond=0 ):
        '''
        Constructor of DateTIme using datetime
        '''
        self.datetime = datetime.datetime(year, month, day, hour, minute, second, microsecond)

    def __str__ (self):
        #print "Values : " + str(self.day) + "/" + str(self.month) + "/" + str(self.year) + " | " + str(self.hour) + ":" + str(self.minute) + ":" + str(self.second) 
        return self.datetime.strftime("%Y-%m-%m %H:%M:%S")
    

    def strftime (self, format_string):         
        return self.datetime.strftime(format_string)



def Date( year, month, day):
    
    date = DateTime(year, month, day)
    print "mx.DateTime implementation of Date : " + date.__str__()
    print "datetime implementation is Date : " + str(datetime.datetime(year,month,day))



def ParseDateTime():
    '''
    the ParseDateTime function of mx.DateTime
    '''
    # TODO complete this
    print "parse date time... "


#######################
#   String <-> Time   #
#######################

def strptime(datetime_string, format_string):
     return datetime.datetime.strptime(datetime_string, format_string)



def RelativeDateTime(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):   
    '''
    years=0,months=0,days=0, year=0,month=0,day=0, hours=0,minutes=0,seconds=0, hour=None,minute=None,second=None, weekday=None,weeks=0
    '''    

    from dateutil.relativedelta import relativedelta

    print "mx.DateTime implementation of RelativeDateTime :  " + (str( mx.DateTime.now() + mx.DateTime.RelativeDateTime(years=years, months=months, weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)))
    print "dateutil implementation of RelativeDateTime : " + (str(datetime.datetime.now() +  relativedelta(years=years, months=months, weeks=weeks, days=days,  hours=hours, minutes=minutes, seconds=seconds)
))


