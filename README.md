# leapyear
Determines if a year or a range of years are leap years (valid for A.D. years).

## Usage
I do not currently have a use for this to run as an independent program so no __name__ == "__main__" is included directly in the leapyear.py file.

## Notes
Years are intended to be entered as any positive integers and should raise exceptions otherwise.  The output is based on leap years from the Gregorian calendar (not established until 1582), as such there are caveats of doing it this way (i.e. different types of calendars, etc).  


## Files & Functions

### leapyear.py

#### leapyear() function
Takes a year as an int.  Returns True if the year is a leap year, False if it is not a leap year.

#### leapyear_range() function
Accepts both a first year and a last year as int's.  Calls leapyear.leapyear() for each year in the range of the first and last year to deterimine if it is a leap year.  If it is a leap year, it appends the year to the leap_years list and returns this list.



### test_leapyear.py

#### test_leapyear() function
Unittests for leapyear.leapyear() function

#### test_leapyear_range() function
Unittests for leapyear.leapyear_range() function
