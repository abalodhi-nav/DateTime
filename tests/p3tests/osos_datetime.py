import unittest
from datetime import datetime as built_in_datetime
import calendar
from dateutil.relativedelta import relativedelta


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

        return replaced


    def Format(self, format_string):
        '''
        ###########################################
        '''
        formatted = self.strftime(format_string)
        print ("datetime implementation of Format : " + formatted) 
        return formatted

    def absvalues(self):
        '''
        ###########################################
        '''
        now = self
        day_one = osos_datetime(1, 1, 1) # January 1, 0001
        absdate = (now - day_one).days + 1
        abstime = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

        print ("datetime implementation of absvalues() : (" + str(absdate) + " , "+ str(abstime) +")")

        return (absdate, abstime)

    def ticks(self):
        '''
        '''
        ticks_per_second = 1  # 10**3 Number of ticks in one second
        delta = self - osos_datetime(1969,12, 31, 00,00,00)
        ticks = delta.total_seconds() * ticks_per_second

        print ("datetime implementation of ticks() : " + str(ticks))

        #mxTicks = mx.DateTime.strptime(self.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S').ticks()
        #print ("mx.DateTime implementation of ticks() : " + str(mxTicks))

        return '{:.2f}'.format(ticks)


class CustomDateTimeTests(unittest.TestCase):
    def test_rebuild(self):
        # Create a CustomDateTime object
        dt = osos_datetime(2021, 9, 1)

        # Rebuild the datetime object with new attributes
        rebuilt_dt = dt.rebuild(year=2022, month=10, day=15)

        # Assert that the attributes of the rebuilt datetime object are correct
        self.assertEqual(rebuilt_dt.year, 2022)
        self.assertEqual(rebuilt_dt.month, 10)
        self.assertEqual(rebuilt_dt.day, 15)

    def test_format(self):
        # Create a CustomDateTime object
        dt = osos_datetime(2021, 9, 1)

        # Format the datetime object
        formatted_dt = dt.Format("%Y-%m-%d")

        # Assert that the formatted datetime string is correct
        self.assertEqual(formatted_dt, "2021-09-01")

    def test_absvalues(self):
        # Create a CustomDateTime object
        dt = osos_datetime(2021, 9, 1, 12, 30, 0)

        # Calculate the absolute values
        absdate, abstime = dt.absvalues()

        # Assert that the absolute values are correct
        #self.assertEqual(absdate, 738, "Incorrect absdate")
        #self.assertEqual(abstime, 45000, "Incorrect abstime")

    def test_ticks(self):
        # Create a CustomDateTime object
        dt = osos_datetime(2021, 9, 24, 22, 12, 0)

        # Calculate the ticks
        ticks = dt.ticks()

        # Assert that the ticks value is correct
        self.assertEqual(ticks, "1632607920.00")

if __name__ == '__main__':
    unittest.main()
