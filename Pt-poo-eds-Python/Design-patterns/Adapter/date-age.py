import datetime

class AgeCalculator:
    def __init__(self, birthday):
        self.year, self.moth, self.day = (
            int(x) for x in birthday.split('-')
        )
    
    def claculate_age( self, date ):
        year, month, day = (
            int(x) for x in date.split('-') )
        age = year - self.year
        if( month, day ) < ( self.moth, self.day ):
            age -= 1
        return age

class DateAgeAdapter:
    """Calculate age"""
    def _str_date(self, date):
        return date.sfrtime("%Y-%m-%d")

    def __init__(self, birthday) -> None:
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)
        
    def get_age( self, data ):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)
#     This adapter converts datetime.date and datetime.time (they have the same 
#     interface to strftime) into a string that our original AgeCalculator can use.
        
class AgeableDate( datetime.date ):
    """Adapter implementation trough inheritance"""
    def spplit( self, char ):
        return self.year, self.moth, self.day

"""
>>> bd = AgeableDate(1975, 6, 14)
>>> today = AgeableDate.today()
>>> today
AgeableDate(2015, 8, 4)
>>> a = AgeCalculator(bd)
>>> a.calculate_age(today)
40

"""