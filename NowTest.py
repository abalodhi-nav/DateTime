import unittest
import datetime
import mx.DateTime

def now():
    '''
    the now function of datetime vs mx.DateTime
    '''
    datetimeNow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
    datetimeNow = datetime.datetime.strptime(datetimeNow, '%Y-%m-%d %H:%M:%S.%f')
    print "datetime implementation of datetime now() : " + str(datetimeNow)

    # TODO comment the following out and return the datetimeNow
    mxDateTime = mx.DateTime.now()
    print "mx.DateTime implementation of datetime now() : " + str(mxDateTime)
    return datetimeNow, mxDateTime

class TestNowFunction(unittest.TestCase):
    def test_datetime_implementation(self):
        # Arrange
        expected = datetime.datetime.now()

        # Act
        actual, _ = now()

        # Assert
        self.assertAlmostEqual(expected, actual, delta=datetime.timedelta(seconds=1))

    def test_mxdatetime_implementation(self):
        # Arrange
        expected = mx.DateTime.now()

        # Act
        _, actual = now()

        # Assert
        self.assertAlmostEqual(expected, actual, delta=datetime.timedelta(seconds=1))

    def test_mxdatetime_equals_datetime(self):
        mxDT, datetimeDT = now()

        self.assertEqual(str(mxDT)[:-4], str(datetimeDT))


if __name__ == '__main__':
    unittest.main()
