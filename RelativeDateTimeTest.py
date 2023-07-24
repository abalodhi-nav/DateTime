import unittest
from datetime import datetime
from dateutil.relativedelta import relativedelta
import mx.DateTime

def RelativeDateTime(years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):
    var = mx.DateTime.now() + mx.DateTime.RelativeDateTime(years=years, months=months, weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    var2 = datetime.now() +  relativedelta(years=years, months=months, weeks=weeks, days=days,  hours=hours, minutes=minutes, seconds=seconds)

    print("mx.DateTime implementation of RelativeDateTime :  " + str(var))
    print("dateutil implementation of RelativeDateTime : " + str(var2))

    return var, var2

class TestRelativeDateTime(unittest.TestCase):
    
    def test_var_equals_var2(self):
        var, var2 = RelativeDateTime()

        self.assertEquals(str(var), str(var2))
    

    def test_relative_date_time(self):
        var, var2 = RelativeDateTime(years=-2, months=3, weeks=1, days=0, hours=4, minutes=30, seconds=20)

        now = mx.DateTime.now()
        self.assertEqual(var.year, now.year -2 )
        self.assertEqual(var.month, (now.month +3 )%12)
        self.assertEqual(var.day, (now.day ))
        self.assertEqual(var.hour, (now.hour + 4)%24 )
        self.assertEqual(var.minute, (now.minute + 30) %60 )
        self.assertEqual(var.second, (now.second + 20)%60)

        now2 = datetime.now()
        self.assertEqual(var2.year, now2.year - 2)
        self.assertEqual(var2.month, (now2.month + 3 )%12)
        self.assertEqual(var2.day, (now2.day ))
        self.assertEqual(var2.hour, (now2.hour + 4)%24 )
        self.assertEqual(var2.minute, (now2.minute + 30) %60 )
        self.assertEqual(var2.second, (now2.second + 20)%60)

    # TODO test seconds from Epic

if __name__ == '__main__':
    unittest.main()
