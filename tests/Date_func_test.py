import unittest
from datetime import datetime as built_in_datetime
import mx.DateTime
import calendar
from dateutil.relativedelta import relativedelta

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
    # Implementation of DateTime class
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
        mx_datetime_formatted = self.datetime.strftime(format_string)

        print("Formatted datetime (using datetime module): " + str(datetime_formatted))
        print("Formatted datetime (using mx.DateTime module): " + str(mx_datetime_formatted))

        return datetime_formatted


def Date(year, month, day):
    # Implementation of Date function

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


class DateTests(unittest.TestCase):
    def test_Date(self):
        # Test case 1: Creating a Date object with a specific date
        date_obj = Date(2022, 12, 31)
        expected_date_obj = datetime(2022, 12, 31)
        self.assertEqual(date_obj, expected_date_obj)
        self.assertEqual(str(date_obj), str(expected_date_obj))
        self.assertIsInstance(date_obj,type( expected_date_obj))
        

        # Test case 2: Creating a Date object with another date
        date_obj = Date(2023, 1, 1)
        expected_date_obj = datetime(2023, 1, 1)
        self.assertEqual(date_obj, expected_date_obj)
        self.assertEqual(str(date_obj), str(expected_date_obj))
        self.assertIsInstance(date_obj,type(expected_date_obj))

        # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
