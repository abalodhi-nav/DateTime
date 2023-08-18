#>>> mx.DateTime.oneDay
#relativedelta(days=+1)

import unittest
from P3 import mx
from dateutil.relativedelta import relativedelta


oneDay = mx.DateTime.oneDay

class OneDayTests(unittest.TestCase):
    def test_one_day(self):
        # Test case 1: Check if oneDay is a relativedelta object with 1 day
        self.assertIsInstance(oneDay, relativedelta)
        print("oneDay is an instance of relativedelta.") 
        self.assertEqual(oneDay.days, 1)
        print("oneDay represents a time delta of 1 day.")

        self.assertEqual(oneDay.months, 0)
        self.assertEqual(oneDay.years, 0)
        print("oneDay does not represent any months or years.")        

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
