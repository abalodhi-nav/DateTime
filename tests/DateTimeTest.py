import unittest
import calendar
from datetime import datetime
import mx.DateTime

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



class DateTimeTests(unittest.TestCase):
    def test_DateTime(self):
        # Test case 1: Creating a DateTime object with a specific date and time
        dt = DateTime(2022, 12, 31, 23, 59, 59)
        expected_dt = datetime(2022, 12, 31, 23, 59, 59)
        self.assertEqual(dt, expected_dt)
        self.assertEqual(dt.day_of_week, expected_dt.weekday())
        self.assertEqual(dt.days_in_month, calendar.monthrange(2022, 12)[1])

        # Test case 2: Creating a DateTime object with default time values
        dt = DateTime(2023, 1, 1)
        expected_dt = datetime(2023, 1, 1)
        self.assertEqual(dt, expected_dt)
        self.assertEqual(dt.day_of_week, expected_dt.weekday())
        self.assertEqual(dt.days_in_month, calendar.monthrange(2023, 1)[1])

        # Test case 3: Testing strftime method
        dt = DateTime(2023, 12, 31, 23, 59, 59)
        format_string = "%Y-%m-%d %H:%M:%S"
        formatted_dt = dt.strftime(format_string)
        expected_dt = datetime(2023, 12, 31, 23, 59, 59)
        expected_formatted_dt = expected_dt.strftime(format_string)
        self.assertEqual(formatted_dt, expected_formatted_dt)

        # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
