import unittest
from datetime import datetime
from my_datetime import CustomDateTime

class CustomDateTimeTests(unittest.TestCase):
    def test_rebuild(self):
        # Create a CustomDateTime object
        dt = CustomDateTime(2021, 9, 1)

        # Rebuild the datetime object with new attributes
        rebuilt_dt = dt.rebuild(year=2022, month=10, day=15)

        # Assert that the attributes of the rebuilt datetime object are correct
        self.assertEqual(rebuilt_dt.year, 2022)
        self.assertEqual(rebuilt_dt.month, 10)
        self.assertEqual(rebuilt_dt.day, 15)

    def test_format(self):
        # Create a CustomDateTime object
        dt = CustomDateTime(2021, 9, 1)

        # Format the datetime object
        formatted_dt = dt.Format("%Y-%m-%d")

        # Assert that the formatted datetime string is correct
        self.assertEqual(formatted_dt, "2021-09-01")

    def test_absvalues(self):
        # Create a CustomDateTime object
        dt = CustomDateTime(2021, 9, 1, 12, 30, 0)

        # Calculate the absolute values
        absdate, abstime = dt.absvalues()

        # Assert that the absolute values are correct
        self.assertEqual(absdate, 738, "Incorrect absdate")
        self.assertEqual(abstime, 45000, "Incorrect abstime")

    def test_ticks(self):
        # Create a CustomDateTime object
        dt = CustomDateTime(2021, 9, 1, 12, 30, 0)

        # Calculate the ticks
        ticks = dt.ticks()

        # Assert that the ticks value is correct
        self.assertEqual(ticks, "1630463400000.00")

if __name__ == '__main__':
    unittest.main()
