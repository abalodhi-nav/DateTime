import unittest
import datetime
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

    def ticks(self):
        '''
        '''
        ticks_per_second = 1  # 10**3 Number of ticks in one second
        delta = self - osos_datetime(1969,12, 31, 00,00,00)
        ticks = delta.total_seconds() * ticks_per_second

        print ("datetime implementation of ticks() : " + str(ticks))

        mxTicks = mx.DateTime.strptime(self.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S').ticks()
        print ("mx.DateTime implementation of ticks() : " + str(mxTicks))

        return '{:.2f}'.format(ticks)

class CustomDateTime(osos_datetime):
    '''
    DateTime class for working with dates and times.
    '''

    def __init__ (self, year, month, day, hour=0, minute=0, second=0, microsecond=0 ):
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

        #mx_datetime_formatted = mx.DateTime.strftime(self.datetime, format_string)
        # AttributeError: 'module' object has no attribute 'strftime'

        print("Formatted datetime (using datetime module): " + str(datetime_formatted))
        #print("Formatted datetime (using mx.DateTime module): " + str(mx_datetime_formatted))

        return datetime_formatted

class CustomDateTimeTests(unittest.TestCase):
    def test_lt_operator_with_none(self):
        # Create a CustomDateTime object
        custom_dt = CustomDateTime(2023, 9, 1, 7, 37, 11, 900000)

        # Test the < operator with None
        result = custom_dt < None

        # Assert that the result is False
        self.assertFalse(result)

    def test_lt_operator_true(self):
        # Create a CustomDateTime object
        custom_dt = CustomDateTime(2023, 9, 1, 7, 37, 11, 900000)

        # Create a regular datetime object
        regular_dt = datetime.datetime(2023, 9, 1, 7, 39, 4, 871195)

        # Test the < operator with a regular datetime object
        result = custom_dt < regular_dt

        # Assert that the result is True
        self.assertTrue(result)

    def test_lt_operator_false(self):
        # Create a CustomDateTime object
        custom_dt = CustomDateTime(2023, 9, 1, 7, 39, 4, 871195)

        # Create a regular datetime object
        regular_dt = datetime.datetime(2023, 9, 1, 7, 37, 11, 900000)

        # Test the < operator with a regular datetime object
        result = custom_dt < regular_dt

        # Assert that the result is False
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
