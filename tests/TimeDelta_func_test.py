import unittest
import mx.DateTime
from dateutil.relativedelta import relativedelta

def TimeDelta(hours=0, minutes=0, seconds=0):
    # Implementation of TimeDelta function
    tim_del = mx.DateTime.TimeDelta(hours=hours, minutes=minutes, seconds=seconds)
    time_delta = relativedelta( hours=hours, minutes=minutes, seconds=seconds)

    print("mx.DateTime implementation of TimeDelta() :  " + str(tim_del) )
    print("dateutil implementation of TimeDelta() : " + str(time_delta) )

    return time_delta

class TimeDeltaTests(unittest.TestCase):
    def test_TimeDelta(self):
        # Test case 1: Calling TimeDelta with default arguments
        delta = TimeDelta()
        expected_delta = relativedelta(hours=0, minutes=0, seconds=0)
        self.assertEqual(delta, expected_delta)
        self.assertIsInstance(delta, relativedelta)

        # Test case 2: Calling TimeDelta with specific arguments
        delta = TimeDelta(hours=1, minutes=30, seconds=45)
        expected_delta = relativedelta(hours=1, minutes=30, seconds=45)
        self.assertEqual(delta, expected_delta)
        self.assertIsInstance(delta, relativedelta)

        # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
