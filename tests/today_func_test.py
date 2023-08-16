import unittest
from datetime import datetime, date
import mx.DateTime

def today():
    '''
    the today function of datetime vs mx.DateTime
    '''
    datetimeToday = date.today()
    # the .today() gives non-zero Time stamp in datetime, hence creating an object this way
    dateToday = datetime(datetimeToday.year, datetimeToday.month, datetimeToday.day)
    print("The datetime implementation is: " + str(dateToday))

    # TODO comment the following and return dateToday
    mxToday = mx.DateTime.today()
    print("mx.DateTime  implementation of datetime today : " + str(mxToday))
    return dateToday, mxToday

class TestToday(unittest.TestCase):

    def test_datetime_today(self):
        expected = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        actual, _ = today()
        self.assertEqual(actual, expected)

    def test_mx_today(self):
        _, expected = today()
        actual = mx.DateTime.now().date
        self.assertEqual(actual, expected.date)

if __name__ == '__main__':
    unittest.main()
