def isleap(year: int) -> bool:
    """Return whether the given year is a leap year"""

    divisible = lambda a, b: a % b == 0

    if not divisible(year, 4):
        return False

    if not divisible(year, 100):
        return True
        
    if not divisible(year, 400):
        return False

    return True


def monthrange(year: int, month: int) -> int:
    """Return the number of days in a given month in specific year"""

    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31

    if month == 2:
        return 29 if isleap(year) else 28

    return 30

def isvalid(year: int, month: int, day: int) -> bool:
    """Return whether given year, month and day form a valid date"""
    
    if (not 1 <= day <= 31 or
            not 1 <= month <= 12 or
            year < 0):
        return False

    # Checking if year, month and day form a valid date
    return day <= monthrange(year, month)


class MiDate(object):
    """
    Comparable date class.

    Attributes:
        year (int): Year part of the date
        month (int): Month part of the date(1 indexed)
        day (int): Day part of the date(1 indexed)
    """

    def __init__(self, year: int, month: int, day: int):
        if not isvalid(year, month, day):
            raise ValueError('Invalid date')

        self.year = year
        self.month = month
        self.day = day

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __lt__(self, other):
        if self.year != other.year:
            return self.year < other.year
        
        if self.month != other.month:
            return self.month < other.month
        
        if self.day != other.day:
            return self.day < other.day
        
        return False

    def __repr__(self):
        return 'MiDate %s' % self.__str__()

    def __str__(self):
        def zeropad(val: int) -> str:
            """Return zero padded number"""
            return str(val) if val > 9 else '0' + str(val)

        return '%s-%s-%s' % (str(self.year), zeropad(self.month), zeropad(self.day))