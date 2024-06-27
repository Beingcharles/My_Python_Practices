year = int(input())
def is_leap(year):
    leap = False
    if not (year % 4):
        if year % 100:
            leap = True
        else:
            if not (year % 400):
                leap = True
    return leap
