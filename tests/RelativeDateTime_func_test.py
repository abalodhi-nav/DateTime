import unittest
from datetime import datetime
from dateutil.relativedelta import relativedelta
import mx.DateTime


def RelativeDateTime(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):
    '''
    '''
    var = mx.DateTime.now() + mx.DateTime.RelativeDateTime(years=years, months=months, weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    delta = relativedelta(years=years, months=months, weeks=weeks, days=days,  hours=hours, minutes=minutes, seconds=seconds, microseconds=0)
    var2 = datetime.now() + delta

    #datetimeNow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
    #datetimeNow = datetime.datetime.strptime(datetimeNow, '%Y-%m-%d %H:%M:%S.%f')
 
    var_str = var.strftime("%Y-%m-%d %H:%M:%S") 
    var2_str = var2.strftime("%Y-%m-%d %H:%M:%S")

    print("mx.DateTime implementation of RelativeDateTime :  " + var_str)
    print("dateutil implementation of RelativeDateTime : " + var2_str)

    return datetime.strptime(var_str, "%Y-%m-%d %H:%M:%S") , datetime.strptime(var2_str, "%Y-%m-%d %H:%M:%S")



class TestRelativeDateTime(unittest.TestCase):
    
    def test_var_equals_var2(self):
        var, var2 = RelativeDateTime()

        self.assertEquals(str(var), str(var2))
    
    def test_RelativeDateTime(self):
        # Test case 1: RelativeDateTime with 1 year
        dt_mx, dt_builtin = RelativeDateTime(years=1)
        expected_mx = mx.DateTime.now() + mx.DateTime.RelativeDateTime(years=1)
        expected_builtin = datetime.now() + relativedelta(years=1)
        self.assertEqual(dt_mx.strftime("%Y-%m-%d %H:%M:%S"), expected_mx.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertEqual(dt_builtin.strftime("%Y-%m-%d %H:%M:%S"), expected_builtin.strftime("%Y-%m-%d %H:%M:%S"))

        # Test case 2: RelativeDateTime with 2 weeks and 3 days
        dt_mx, dt_builtin = RelativeDateTime(weeks=2, days=3)
        expected_mx = mx.DateTime.now() + mx.DateTime.RelativeDateTime(weeks=2, days=3)
        expected_builtin = datetime.now() + relativedelta(weeks=2, days=3)
        self.assertEqual(dt_mx.strftime("%Y-%m-%d %H:%M:%S"), expected_mx.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertEqual(dt_builtin.strftime("%Y-%m-%d %H:%M:%S"), expected_builtin.strftime("%Y-%m-%d %H:%M:%S"))
        
        # Test case 3: RelativeDateTime with 1 hour and 30 minutes
        dt_mx, dt_builtin = RelativeDateTime(hours=1, minutes=30)
        expected_mx = mx.DateTime.now() + mx.DateTime.RelativeDateTime(hours=1, minutes=30)
        expected_builtin = datetime.now() + relativedelta(hours=1, minutes=30)
        self.assertEqual(dt_mx.strftime("%Y-%m-%d %H:%M:%S"), expected_mx.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertEqual(dt_builtin.strftime("%Y-%m-%d %H:%M:%S"), expected_builtin.strftime("%Y-%m-%d %H:%M:%S"))

        # Test case 4: RelativeDateTime with negative values
        dt_mx, dt_builtin = RelativeDateTime(years=-1, months=-6, days=-15)
        expected_mx = mx.DateTime.now() + mx.DateTime.RelativeDateTime(years=-1, months=-6, days=-15)
        expected_builtin = datetime.now() + relativedelta(years=-1, months=-6, days=-15)
        self.assertEqual(dt_mx.strftime("%Y-%m-%d %H:%M:%S"), expected_mx.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertEqual(dt_builtin.strftime("%Y-%m-%d %H:%M:%S"), expected_builtin.strftime("%Y-%m-%d %H:%M:%S"))

        # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
