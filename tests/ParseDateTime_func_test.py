import unittest
from datetime import datetime
import mx.DateTime

def ParseDateTime(date_str):
    # Implementation of ParseDateTime function
    parsedDT = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    print 'datetime implementation of ParseDateTime() : ' + str(parsedDT)

    print 'mx.DateTime implementation of ParseDateTime() : '  + str(mx.DateTime.ISO.ParseDateTime(date_str))

    return parsedDT


class ParseDateTimeTests(unittest.TestCase):
    def test_ParseDateTime(self):
        # Test case 1: Parsing a valid date string
        date_str = "2022-12-31 23:59:59"
        parsed_dt = ParseDateTime(date_str)
        expected_dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        self.assertEqual(parsed_dt, expected_dt)


        # Test case 2: Parsing a valid date string
        date_str = "2022-12-31 23:59:59"
        parsed_dt = ParseDateTime(date_str)
        expected_dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S') #%y takes only year in double digits
        self.assertEqual(parsed_dt, expected_dt)


        # Test case 3: Parsing an invalid date string
        date_str = "2022-13-31 23:59:59"  # Invalid month (13)
        with self.assertRaises(ValueError):
            parsed_dt = ParseDateTime(date_str)

        # Test case 4: Parsing a date string with a different format
        date_str = "2022/12/31 23:59:59"  # Different format (slashes instead of dashes)
        with self.assertRaises(ValueError):
            parsed_dt = ParseDateTime(date_str)

        # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
