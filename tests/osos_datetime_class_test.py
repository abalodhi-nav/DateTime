import mx.DateTime
from datetime import datetime as built_in_datetime
import unittest
import calendar
from dateutil.relativedelta import relativedelta

class CustomDateTime(built_in_datetime):
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
        hour = current_date.hour if hour is None else int(hour)
        minute = current_date.minute if minute is None else int(minute)
        second = current_date.second if second is None else int(second)

        replaced = current_date.replace(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

        print ("datetime implementation of rebuild() : " + str(replaced) )
        print ("mx.DateTime implementation of rebuild() : " + str(mx.DateTime.now().rebuild(year=year, month=month, day=day, hour=hour, minute=minute, second=second)))

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
        day_one = built_in_datetime(1, 1, 1) # January 1, 0001
        absdate = (now - day_one).days + 1 
        abstime = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        
        print ("datetime implementation of absvalues() : (" + str(absdate) + " , "+ str(abstime) +")")

        print ("mx.DateTime implementation of absvalues() : " + str(mx.DateTime.now().absvalues()))
        
        return (absdate, abstime)



# Rest of the code...
class CustomDateTimeTests(unittest.TestCase):
    def test_rebuild(self):
        # Create a CustomDateTime object
        dt = CustomDateTime(2023, 1, 1)

        # Call the rebuild method with new attributes
        rebuilt_dt = dt.rebuild(year=2024, month=2, day=2, hour=14, minute=3, second=59)

        # Assert that the attributes have been updated correctly
        self.assertEqual(rebuilt_dt.year, 2024)
        self.assertEqual(rebuilt_dt.month, 2)
        self.assertEqual(rebuilt_dt.day, 2)
        self.assertEqual(rebuilt_dt.hour, 14)
        self.assertEqual(rebuilt_dt.minute, 3)
        self.assertEqual(rebuilt_dt.second, 59)

    def test_Format(self):
        # Create a CustomDateTime object
        dt = CustomDateTime(2023, 1, 1)

        # Call the Format method with a format string
        formatted_dt = dt.Format("%Y-%m-%d")

        # Assert that the formatted string is correct
        self.assertEqual(formatted_dt, "2023-01-01")

    def test_absvalues(self):
        # Create a CustomDateTime object
        dt = CustomDateTime(2023, 1, 1, 12, 30, 45)

        # Call the absvalues method
        abs_values = dt.absvalues()

        # Assert the returned values are correct
        self.assertEqual(abs_values, (738521, 45045.0))

if __name__ == '__main__':
    unittest.main()
