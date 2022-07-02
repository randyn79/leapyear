#!/usr/bin/env python3

def leapyear(year: int) -> bool:
    """Accepts a year as an int.  Returns True if the year is a leap year,
    False if it is not a leap year."""

    # Check to see if the year is a positive integer.
    if type(year) != int:
        raise TypeError('Input must be an integer')
    if year < 1:
        raise ValueError('Input must be greater than zero')
    
    # If a year is evenly divisible by 100, it must also be equally
    # divisible by 400 in order to be a leap year.
    if year % 100 == 0:
        return year % 400 == 0

    # If a year is not evenly divisible by 100, it must be evenly
    #divisble by 4 in order to be a leap year.
    elif year % 4 == 0:
        return year % 4 == 0

    # If it does not meet the above conditions, it is not a leap year.
    else:
        return False
    
def leapyear_range(first: int, last: int) -> list:
    """Accepts both a first year and a last year as int's.  Calls
    leapyear() for each year in the range of the first and last year
    to determine if it is a leap year.  If it is a leap year, it appends
    the year to the leap_years list and returns this list."""
    leap_years = []

    # Check to see if first and last are positive integers.
    if type(first) != int or type(last) != int:
        raise TypeError('Input must be an integer')
    if first < 1 or last < 1:
        raise ValueError('Input must be greater than zero')

    # If first is larger than last, switch them.
    if first >= last:
        first, last = last, first

    for year in range(first, last+1):
        result = leapyear(year)

        if result == True:
            leap_years.append(year)

    return leap_years



            

        
    
