from datetime import date

MonthsNumberOfDays = [31,30,31,30,31,30,31,31,30,31,30,31]

Day = date.today().day
Month = date.today().month
Year = date.today().year

# Checking if the year is a leap year or not  
def is_leap_year(year):
    test = True
    if (year // 2) % 2 == 1:
        return False

    if not((year % 4 == 0) or (year % 100 == 0) or (year % 100 == 0 and year % 4 == 0)):
        test = False

    if (year % 100 == 0) and (year % 400 != 0):
        return False

    return test

# Another leap year checker function
def leap_year(year):
    test = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                test = True
            else:
                test = False
        else:
            test = True
    else:
        test = False

    return test


# Number of leap years between birthday and today
def LeapYearsTotal(year):
    sum = 0
    for i in range(year, 2022):
        if is_leap_year(i) == True:
            sum += 1

    return sum
    

# Number of days till today
def NumberOfDaysTillToday(year, month, day):
    sum = 0

    for i in range(1,year):
        if is_leap_year(i) == True:
            sum += 366
        else :
            sum += 365

    for i in range(1,month):
        sum += MonthsNumberOfDays[i]

    sum += day

    return sum


# Number of days till birthday
def NumberOfDaysTillBirthday(year, month, day):
    sum = 0

    for i in range(1,year):
        if is_leap_year(i) == True:
            sum += 366
        else :
            sum += 365

    for i in range(1,month):
        sum += MonthsNumberOfDays[i]

    sum += day

    return sum


def AgeCalc(year, month, day):
    N1 = NumberOfDaysTillToday(Year, Month, Day)
    N2 = NumberOfDaysTillBirthday(year, month, day)

    difference = N1 - N2

    dOld = 0
    mOld = 0
    yOld = 0

    LPY = LeapYearsTotal(year)

    while LPY > 1:
        difference -= 366
        LPY -= 1 
        yOld += 1

    while difference > 365:
        difference -= 365
        yOld += 1


    index = 0
    while difference > 30:
        difference -= MonthsNumberOfDays[index]
        mOld += 1

    dOld = difference

    return (yOld, mOld, dOld)
