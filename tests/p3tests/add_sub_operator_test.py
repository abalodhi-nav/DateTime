import unittest
from datetime import datetime as built_in_datetime
from datetime import timedelta
import calendar
from dateutil.relativedelta import relativedelta

dummy_var_type_timedelta = type(timedelta(1))

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

    def __sub__(self, other):
        if type(other) in [int,float, dummy_var_type_timedelta]:
            try:
                return built_in_datetime.__sub__(self,timedelta(days=other))
            except Exception, e:
                print (str(e))
                raise e
            else:
                print("METHOD: osos_datetime subtraction operator for integers\n")
        else:
            raise TypeError("unsupported operand type(s) for -: 'osos_datetime' and '{}'".format(type(other).__name__))
        return built_in_datetime.__sub__(self,other)

    def __add__(self, other):
        if type(other) in [int,float]:
            try:
                return built_in_datetime.__add__(self,timedelta(days=other))
            except Exception, e:
                print("FAILED: " +str(e))
                raise e
        else:
            raise TypeError("unsupported operand type(s) for -: 'osos_datetime' and '{}'".format(type(other).__name__))
        return built_in_datetime.__add__(self,other)


class TestOsosDatetime(unittest.TestCase):
    def setUp(self):
        self.custom_dt = osos_datetime(2023, 9, 11, 1, 2, 3)

    # - operator
    def test_subtraction_operator_with_integer(self):
        # Arrange
        days_to_subtract = 5
        expected_result = osos_datetime(2023, 9, 6, 1, 2, 3)#self.custom_dt - timedelta(days=days_to_subtract)

        # Act
        result = self.custom_dt.__sub__(days_to_subtract)

        # Assert
        self.assertEqual(result, expected_result)

    def test_subtraction_operator_with_invalid_type(self):
        # Arrange
        invalid_type = "invalid"

        # Act & Assert
        with self.assertRaises(TypeError) as context:
            self.custom_dt.__sub__(invalid_type)
        self.assertEqual(str(context.exception), "unsupported operand type(s) for -: 'osos_datetime' and 'str'")

    # + operator 

    def test_addition_operator_with_integer(self):
        # Arrange
        days_to_add = 10
        expected_result = osos_datetime(2023, 9, 21, 1, 2, 3)#self.custom_dt + timedelta(days=days_to_add)

        # Act
        result = self.custom_dt.__add__(days_to_add)

        # Assert
        self.assertEqual(result, expected_result)

    def test_addition_operator_with_invalid_type(self):
        # Arrange
        invalid_type = "invalid"

        # Act & Assert
        with self.assertRaises(TypeError) as context:
            self.custom_dt.__add__(invalid_type)
        self.assertEqual(str(context.exception), "unsupported operand type(s) for -: 'osos_datetime' and 'str'")

if __name__ == '__main__':
    unittest.main()
