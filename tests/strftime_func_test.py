import unittest
from datetime import datetime

def strftime(date_object, format_string='%c'):
    # Implementation of strftime function
    datetime_formatted = datetime.strftime(date_object, format_string)
    # mx_datetime = mx.DateTime.DateTimeFromTicks(date_object)
    # mx_datetime_formatted = mx.DateTime.strftime(date_object, format_string)

    print("datetime implementation of strftime() : " + str(datetime_formatted))
    #print("Formatted datetime (using mx.DateTime module): " + str(mx_datetime_formatted))

    return datetime_formatted


class StrftimeTests(unittest.TestCase):
    def test_strftime_default_format(self):
        # Test case 1: Default format
        date_object = datetime(2022, 1, 1, 12, 34, 56)
        formatted_datetime = strftime(date_object)
        expected_formatted_datetime = "Sat Jan  1 12:34:56 2022"
        self.assertEqual(formatted_datetime, expected_formatted_datetime)
        self.assertIsInstance(formatted_datetime, str)

    def test_strftime_custom_format(self):
        # Test case 2: Custom format
        date_object = datetime(2022, 1, 1, 12, 34, 56)
        format_string = "%Y-%m-%d %H:%M:%S"
        formatted_datetime = strftime(date_object, format_string)
        expected_formatted_datetime = "2022-01-01 12:34:56"
        self.assertEqual(formatted_datetime, expected_formatted_datetime)
        self.assertIsInstance(formatted_datetime, str)


    def test_strftime_special_characters(self):
        # Test case 3: Format with special characters
        date_object = datetime(2022, 1, 1, 12, 34, 56)
        format_string = "Today is %A, %b %d, %Y. The time is %I:%M %p."
        formatted_datetime = strftime(date_object, format_string)
        expected_formatted_datetime = "Today is Saturday, Jan 01, 2022. The time is 12:34 PM."
        self.assertEqual(formatted_datetime, expected_formatted_datetime)
        self.assertIsInstance(formatted_datetime, str)


    def test_strftime_timezone(self):
        # Test case 4: Timezone format
        date_object = datetime(2022, 1, 1, 12, 34, 56)
        format_string = "%Y-%m-%d %H:%M:%S %Z"
        formatted_datetime = strftime(date_object, format_string)
        expected_formatted_datetime = "2022-01-01 12:34:56 "
        self.assertEqual(formatted_datetime, expected_formatted_datetime)
        self.assertIsInstance(formatted_datetime, str)

        # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
