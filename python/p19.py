# 1 january     31
# 2 febuary     28/29
# 3 march       31
# 4 april       30
# 5 may         31
# 6 june        30
# 7 july        31
# 8 august      31
# 9 september   30
# 10 october    31
# 11 november   30
# 12 december   31




class Day():
    def __init__(self, day=1, month=1, year=1900, day_of_week=2):
        self.day = day
        self.month = month
        self.year = 1900
        self.day_of_week = day_of_week
    
    def advance_one_day(self):
        self.day += 1
        self.day_of_week = self.day_of_week % 7 + 1
        month_length = 31
        if self.month in [4, 6, 9, 11]:
            month_length = 30
        if self.month == 2 :
            month_length = 28
            if self.year % 4 == 0 and (self.year % 100 > 0 or self.year % 400 == 0):
                month_length = 29
        if self.day > month_length:
            self.month += 1
            self.day = 1
        if self.month > 12:
            self.year += 1
            self.month = 1

day = Day()

first_month_sundays = 0

while day.year <= 2000:
    if day.day_of_week == 1 and day.day == 1 and day.year >= 1901:
        first_month_sundays += 1
    day.advance_one_day()
    
print first_month_sundays
