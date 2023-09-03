'''
Leap Years

In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:
- years divisible by 4 are leap years
- years divisible by 100 are NOT leap years
- years divisible by 400 are leap years

Additional notes:
- Only valid years (positive integers) will be tested, so you don't have to validate them.
'''

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# More concise solutions from other users
# def is_leap_year(year):
#     return (year % 100 and not year % 4) or not year % 400

# def is_leap_year(year):
#     return False if year % 100 == 0 and year % 400 != 0 else year % 4 == 0
