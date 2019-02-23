#! /usr/bin/env python3

'''OPS435 Assignment 1 - Winter 2019
Program: a1_hwhamidi.py
Author: "Hekmat Hamidi"
The python code in this file (a1_hwhamidi.py) is original work written by
"Hekmat Hamidi". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.'''

import sys




def valid_date(valid):
    '''This function will return error message if the given month or day is not in the calender

    for e.g. 20190199 -> will result in [Error: wrong day]
    and e.g. 20199901 -> will result in [Error: wrong month]

    END'''
    if valid == 1:
        a = "Error: wrong month entered"
    if valid == 2:
        a = "Error: wrong day entered"
    if valid == 3:
        a = "Error: wrong date entered"
    return a



def usage():
    '''Usage Function -> notifies users to on how to use the program.
    If the user enters invalid date (YYYYMMDD) or invalid pramater
    e.g -step instead of --step OR 20191301 -> there are only 12 months in a year OR 20190155
    END'''

    return '''Usage: a1_hwhamidi.py (YYYYMMDD) +/-Day
e.g. -> 20190101 +1 = 20190102

*Using --step parameter*

[./a1_hwhamidi.py --step (YYYYMMDD) +/- Days]
e.g. -> [./a1_hwhamidi.py --step 20190101 5]
-> 20190102
-> 20190103
-> 20190104
-> 20190105
-> 20190106

*Calculate the # of days*

[./a1_hwhamidi.py (YYYYMMDD) (YYYYMMDD)
e.g. -> [./a1_hwhamidi.py 19960101 19970101]
-> 366'''

def yesterday(today):
    '''This function takes the parameter (toda) as (YYYYMMDD) and outputs yesterda's day
    for e.g. 20190101 -> 20181231
    This function splits the given date into year -> [YYYY], month -> [MM], and day -> [DD]

    Sets of condition needs to be met for this function to work.

    1. The given day should not exceed the day in the calender dictionary. This will cause an error
    2. If the given day is minimum in the calender, the month would be changed -> month = month -1
    3. If the month is less the january (1), the year would be changed -> year = year - 1

    END'''
    year = int(today[:4]) # splits the given date (YYYYMMDD) to (YYYY) assigns it to year.
    month = int(today[4:6])	#splits the given date (YYYYMMDD) to (MM) assigns it to month.
    if month > 12:
        print(valid_date(1))
        sys.exit()
    day = int(today[6:]) #splits the given date (YYYYMMDD) to the (DD) assigns it to day.
    if year % 4 == 0: # Checks if the given year is leap year or not.
        feb = 29
    else:
        feb = 28
    if year % 100 == 0:
        feb = 28
    if year % 400 == 0:
        feb = 29
    yesterday = day - 1
    cal = { 1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if day > cal[month]:
        print(valid_date(2))
        sys.exit()
    if yesterday < 1: # goes to previews month if yesterday is less than 1
        month = month -1
        temp_month = month
        if temp_month == 0:
            temp_month = 12
        yesterday = cal[temp_month]
    else:
        month = month + 0
    if month < 1: #goes to previous year if month is less than 1 (January)
        year = year - 1
        month = 12
        yesterday = cal[month]
    else:
        year = year + 0
        yesterday = yesterday
    return (str(year) + str(month).zfill(2) + str(yesterday).zfill(2))

def tomorrow(today):
    '''This function takes the parameter (today) as (YYYYMMDD) and outputs tomorrow's day
    for e.g. 20181231 -> 20190101
    This function splits the given date into year -> [YYYY], month -> [MM], and day -> [DD]
    The date is tomorrow variable then becomes the given date + 1 -> tomorrow = (YYYYMMDD) + 1

	Sets of condition needs to be met for this function to work.

	1. The given day should not exceed the day in the calender dictionary. This will cause an error
	2. If the given day is max in the calender, the month would be changed -> month = month + 1
	3. If the month exceeds the month in the calender, the year would be changed -> year = year + 1

    END'''

    if len(today) != 8:
        print(valid_date(3))
        sys.exit()
    year = int(today[:4])
    month = int(today[4:6])
    if month > 12:
        print(valid_date(1))
        sys.exit()
    day = int(today[6:])
    if year % 4 == 0:
        feb = 29
    else:
        feb = 28
    if year % 100 == 0:
        feb = 28
    if year % 400 == 0:
        feb = 29
    tomorrow = day + 1
    cal = { 1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if day > cal[month]:
        print(valid_date(2))
        sys.exit()
    if tomorrow  > cal[month]:
        month = month + 1
        temp_month = month
        if temp_month == 13:
            temp_month = 1
        tomorrow = 1
    else:
        month = month + 0
    if month > 12:
        year = year + 1
        month = 1
        tomorrow = 1
    else:
        year = year + 0
        tomorrow = tomorrow
    next_day = (str(year) + str(month).zfill(2) + str(tomorrow).zfill(2))
    return next_day
##########DBDA#################################################

def dbda(yyyymmdd, days):
    '''The dbda function takes two parameters, date -> (YYYYYMMDD) and days -> (days)
    If the days given is greater than 0 -> (days > 0), the function calls the tomorrow's function.
    For e.g [./a1_hwhamidi.py 20190101 5] -> 20190106

    If the days given is less than 0 -> (days < 0), the function calls the yesterday's function.
    For e.g. [./a1_hwhamidi.py 20190106 -5] -> 20190101

    END'''

    if int(days) > 0:
       for i in range(int(days)):
           yyyymmdd = tomorrow(yyyymmdd)
    if int(days) < 0:
       for i in range(abs(int(days))):
           yyyymmdd = yesterday(yyyymmdd)
    return yyyymmdd

def bonus():
    '''This function will take two arguments as (YYYYMMDD) and (YYYYMMDD), compares them and prints out the day difference
    for e.g. [./a1_hwhamidi.py 19960101 19970101]
    -> 366
    END'''
    if len(sys.argv) == 2:
        print(valid_date(3))
    if len(sys.argv) == 3:
        days = sys.argv[2]
        yyyymmdd = sys.argv[1]
        if len(days) == 8 and len(yyyymmdd) == 8:
            if int(days) > int(yyyymmdd):
                counter = 0
                while int(days) != int(yyyymmdd):
                    yyyymmdd = tomorrow(yyyymmdd)
                    counter = counter + 1
                print(str(counter))
                sys.exit()
            if int(days) < int(yyyymmdd):
                counter = 0
                while int(days) != int(yyyymmdd):
                    yyyymmdd = yesterday(yyyymmdd)
                    counter = counter + 1
                print(str(counter))
                sys.exit()
        if len(yyyymmdd) != 8:
            print(valid_date(3))
        if len(yyyymmdd) == 8:
            print(dbda(yyyymmdd, days))
    if len(sys.argv) == 4:
        step = sys.argv[1]
        yyyymmdd = sys.argv[2]
        days = sys.argv[3]
        if step == '--step':
            if int(days) > 0:
                for i in range(int(days)):
                    yyyymmdd = tomorrow(yyyymmdd)
                    print(yyyymmdd)
            if int(days) < 0:
                for i in range(abs(int(days))):
                    yyyymmdd = yesterday(yyyymmdd)
                    print(yyyymmdd)

################# MAIN ####################################
if __name__ == "__main__":
    bonus()
