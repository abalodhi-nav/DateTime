import unittest
from datetime import datetime as built_in_datetime
from dateutil.relativedelta import relativedelta
import mx.DateTime

def RelativeDate(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):
    # Implementation of RelativeDate function
    var = mx.DateTime.now() + mx.DateTime.RelativeDate(years=years, months=months, weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    delta = relativedelta(years=years, months=months, weeks=weeks, days=days,  hours=hours, minutes=minutes, seconds=seconds, microseconds=0)

    var2 = built_in_datetime.now() + delta

    var_str = var.strftime("%Y-%m-%d %H:%M:%S")
    var2_str = var2.strftime("%Y-%m-%d %H:%M:%S")

    print("mx.DateTime implementation of RelativeDate() :  " + var_str)
    print("dateutil implementation of RelativeDate() : " + var2_str)

    return delta


def RelativeDateTimeDiff(date1=None, date2=None):
    # Implementation of RelativeDateTimeDiff function
    # Check if both dates are provided
    if date1 is None or date2 is None:
        raise ValueError("Both date1 and date2 must be provided.")

    # Calculate the difference between the two dates
    rel_del = relativedelta(date1, date2)

    print("mx.DateTime implementation of RelativeDateTimeDiff() :  " + str(mx.DateTime.RelativeDateTimeDiff(mx.DateTime.DateTime(date1.year, date1.month, date1.day, date1.hour, date1.minute, date1.second), (mx.DateTime.DateTime(date2.year, date2.month, date2.day, date2.hour, date2.minute, date2.second)) )))
    print("dateutil implementation of RelativeDateTimeDiff() : " + str(rel_del) )

    return rel_del


def RelativeDateDiff(date1=None, date2=None):
    # Implementation of RelativeDateDiff function
    # Check if both dates are provided
    if date1 is None or date2 is None:
        raise ValueError("Both date1 and date2 must be provided.")

    # Calculate the difference between the two dates
    rel_del = relativedelta(date1, date2)

    print("mx.DateTime implementation of RelativeDateDiff() :  " + str(mx.DateTime.RelativeDateTimeDiff(mx.DateTime.DateTime(date1.year, date1.month, date1.day, date1.hour, date1.minute, date1.second), (mx.DateTime.DateTime(date2.year, date2.month, date2.day, date2.hour, date2.minute, date2.second)) )))
    print("dateutil implementation of RelativeDateDiff() : " + str(rel_del) )

    return rel_del



class RelativeDateTests(unittest.TestCase):
    def test_RelativeDate(self):
        # Test case 1: Calling RelativeDate with default arguments
        current_datetime = built_in_datetime.now()
        delta = RelativeDate()
        expected_datetime = current_datetime + relativedelta(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0)
        self.assertEqual(current_datetime+delta, expected_datetime)
        self.assertIsInstance(delta, relativedelta)

        # Test case 2: Calling RelativeDate with specific arguments
        delta = RelativeDate(years=1, months=2, weeks=3, days=4, hours=5, minutes=6, seconds=7)
        expected_datetime = current_datetime + relativedelta(years=1, months=2, weeks=3, days=4, hours=5, minutes=6, seconds=7, microseconds=0)
        self.assertEqual(current_datetime+ delta, expected_datetime)
        self.assertIsInstance(delta, relativedelta)

        # Add more test cases as needed...

    def test_RelativeDateTimeDiff(self):
        # Test case 1: Calling RelativeDateTimeDiff with valid date1 and date2
        date1 = built_in_datetime(2022, 1, 1, 0, 0, 0)
        date2 = built_in_datetime(2023, 1, 1, 0, 0, 0)
        delta = RelativeDateTimeDiff(date1, date2)
        expected_delta = relativedelta(date1, date2)
        self.assertEqual(delta, expected_delta)
        self.assertIsInstance(delta, relativedelta)

        # Test case 2: Calling RelativeDateTimeDiff with invalid date1 and date2 (both None)
        with self.assertRaises(ValueError):
            RelativeDateTimeDiff()

        # Add more test cases as needed...

    def test_RelativeDateDiff(self):
        # Test case 1: Calling RelativeDateDiff with valid date1 and date2
        date1 = built_in_datetime(2022, 1, 1)
        date2 = built_in_datetime(2023, 1, 1)
        delta = RelativeDateDiff(date1, date2)
        expected_delta = relativedelta(date1, date2)
        self.assertEqual(delta, expected_delta)
        self.assertIsInstance(delta, relativedelta)

        # Test case 2: Calling RelativeDateDiff with invalid date1 and date2 (both None)
        with self.assertRaises(ValueError):
            RelativeDateDiff()

        # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
