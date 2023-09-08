import unittest
from datetime import datetime as built_in_datetime
import calendar
from dateutil.relativedelta import relativedelta


class osos_datetime(built_in_datetime):
    '''
    A custom datetime class that inherits from the built-in datetime.datetime class.
    '''
    def __new__(cls, *args, **kwargs):
            return super(osos_datetime, cls).__new__(cls, *args, **kwargs)


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

        print ("datetime implementation of rebuild() : " + str(replaced) )
        # print ("mx.DateTime implementation of rebuild() : " + str(mx.DateTime.now().rebuild(year=year, month=month, day=day) ))

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
        # print ("mx.DateTime implementation of absvalues() : " + str(mx.DateTime.now().absvalues()))
        
        return (absdate, abstime)

    def ticks(self):
        '''
        '''
        ticks_per_second = 1  # 10**3 Number of ticks in one second
        delta = self - osos_datetime(1969,12, 31, 00,00,00)
        ticks = delta.total_seconds() * ticks_per_second

        print ("datetime implementation of ticks() : " + str(ticks))
        
        # mxTicks = mx.DateTime.strptime(self.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S').ticks()
        #print ("mx.DateTime implementation of ticks() : " + str(mxTicks))

        return '{:.2f}'.format(ticks)





class TestOsosDatetime(unittest.TestCase):
    def setUp(self):
        self.custom_dt = osos_datetime(2023, 9, 1, 7, 39, 4)

    def test_rebuild(self):
        # Arrange
        year = 2024
        month = 10
        day = 15

        # Act
        rebuilt_dt = self.custom_dt.rebuild(year=year, month=month, day=day)

        # Assert
        self.assertEqual(rebuilt_dt.year, year)
        self.assertEqual(rebuilt_dt.month, month)
        self.assertEqual(rebuilt_dt.day, day)

    def test_format(self):
        # Arrange
        format_string = "%Y-%m-%d %H:%M:%S"

        # Act
        formatted_str = self.custom_dt.Format(format_string)

        # Assert
        self.assertEqual(formatted_str, "2023-09-01 07:39:04")

    def test_absvalues(self):
        # Act
        absdate, abstime = self.custom_dt.absvalues()

        # Assert
        self.assertEqual(absdate, 738764)
        self.assertEqual(abstime, 27544.0)

    def test_ticks(self):
        # Act
        ticks = self.custom_dt.ticks()

        # Assert
        self.assertEqual(ticks, '1693640344.00')


if __name__ == '__main__':
    unittest.main()
