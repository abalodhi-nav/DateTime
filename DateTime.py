import datetime
import os

def setPythonPath():
    new_path = "/home/src/components:/home/src/custom/ajb/osos/middleTier:/home/src/custom/ajb/osos/config:/home/src/custom/ajb/osos/middleTier/osos:/home/src/custom/ajb/osos/middleTier/domains:/home/src/custom/ajb/osos/selfService/src:/home/src/custom/ajb/osos/admin/src:/home/src/custom/ajb/osos/reports:/home/src/components/restful/src:/usr/lib/python2.7/dist-packages:/usr/local/lib/python2.7/dist-packages"
    if new_path not in os.environ.get(['PYTHONPATH'], '').split(os.pathsep):
        os.environ["PYTHONPATH"] = new_path + os.pathsep + os.environ.get('PYTHONPATH','')

def now():
    '''
    the two different dateTimes 
    '''
    datetimeNow = datetime.datetime.now()
    print "Python3 implementation of datetime now() : " + str(datetimeNow)
    print "Python3 year : " + str(datetimeNow.year)
    print "Python3 strftime : " + str(datetimeNow.strftime("%I%M%p"))



    import mx.DateTime 
    print "Python2 implementation of datetime now() : " + str(mx.DateTime.now())
    print "Python2 implementation of datetime with format : " + str(mx.DateTime.now().Format('%m/%d/%Y'))

    print "Python2 format " + mx.DateTime.now().Format('%m/%d/%Y %H:%M:%S')

    print "Python2 format days " + (mx.DateTime.now() + mx.DateTime.RelativeDateTime(days=+365)).strftime("%m%d%Y") 

    print "Python2 format year" + (mx.DateTime.now() + mx.DateTime.RelativeDateTime(years=14)).strftime("%m%d%Y") 

    print "Python2 format now stftime : " + mx.DateTime.now().strftime("%I%M%p")

    print "Python2 object creation DateTiem : " + str(mx.DateTime.DateTime(2023, 6, 9))


    #print "Python2 object creation Date : " + mx.DateTime.Date(2023, 6, 9)

def today():
    
    '''
    the two different dateTimes
    '''
    datetimeToday = datetime.datetime.today()
    print "Python3 implementation of datetime today : " + str(datetimeToday)


    import mx.DateTime
    print "Python2  implementation of datetime today : " + str(mx.DateTime.today())


