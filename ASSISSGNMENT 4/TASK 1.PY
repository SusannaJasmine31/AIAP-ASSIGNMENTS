def is_leap_year(year):
    """
    Return True if `year` is a leap year (Gregorian rules).
    A year is a leap year if it's divisible by 4, except years divisible by 100
    which are not leap years unless divisible by 400.
    """
    if not isinstance(year, int):
        raise TypeError("year must be an integer")
    if year <= 0:
        raise ValueError("year must be positive")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == "__main__":
    for y in (2000, 1900, 2020, 2023):
        print(f"{y}: {'leap year' if is_leap_year(y) else 'not a leap year'}")