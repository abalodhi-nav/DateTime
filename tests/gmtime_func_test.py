import unittest
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import mx.DateTime

def gmtime(date=datetime.utcnow(), tzone_offset_in_min=0):
    # Implementation of gmtime function
    '''
    Custom gmtime() function that calculates the local time given a UTC datetime and timezone offset.

    Parameters:
        date (datetime.datetime): The UTC datetime object. Defaults to the current UTC datetime.
        tzone_offset_in_min (int): The timezone offset in minutes. Defaults to 0 (no offset).

    #########################################################################################
    Returns:
        datetime.datetime: The local datetime object based on the provided UTC datetime and timezone offset.
    '''

    gm_datetime = date  + relativedelta(minutes=tzone_offset_in_min)
    print("mx.DateTime implementation of gmtime() :  " + str(mx.DateTime.gmtime() + mx.DateTime.TimeDelta(minutes=tzone_offset_in_min)))
    print("datetime implementation of gmtime() : " + str(gm_datetime) )

    return gm_datetime


class GmtimeTests(unittest.TestCase):
    def test_gmtime(self):
        # Test case 1: Calling gmtime with default arguments
        current_utc = datetime.utcnow()
        gmtime_obj = gmtime()
        expected_gmtime_obj = current_utc + timedelta(minutes=0)
        self.assertEqual(gmtime_obj.strftime("%Y-%m-%d %H:%M:%S"), expected_gmtime_obj.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertEqual(str(gmtime_obj.strftime("%Y-%m-%d %H:%M:%S")), str(expected_gmtime_obj.strftime("%Y-%m-%d %H:%M:%S")))
        self.assertIsInstance(gmtime_obj, datetime)

        # Test case 2: Calling gmtime with specific UTC datetime and timezone offset
        utc_datetime = datetime(2022, 12, 31, 23, 59, 59)
        offset = 120  # 2 hours offset
        gmtime_obj = gmtime(utc_datetime, offset)
        expected_gmtime_obj = utc_datetime + timedelta(minutes=offset)
        self.assertEqual(gmtime_obj, expected_gmtime_obj)
        self.assertEqual(str(gmtime_obj), str(expected_gmtime_obj))
        self.assertIsInstance(gmtime_obj, datetime)

        # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
