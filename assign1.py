#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2022

Program: assign1.py
Author: "Student Full Name" - "Student ID"

The python code in this file (assign1.py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

Date: 2022-02-06
'''

def usage():
    "TODO enter docstring"
    pass # TODO: delete this line, replace with valid code.

def days_in_mon(year):
    "TODO enter docstring"
    # return dictionary_months
    pass # TODO: delete this line, replace with valid code.

def valid_date(date):
    "TODO enter docstring"
    # return True or False 
    pass # TODO: delete this line, replace with valid code.

def leap_year(year):
    "takes a year in YYYY format, and returns True if it's a leap year, False otherwise."
    # TODO reorganize code, enter code from after() here.
    pass # TODO: delete this line, replace with return statement.


def after(today):
    "after takes a valid date string in DD-MM-YYYY format and returns"
    "a date string for the next day in DD-MM-YYYY format."
    if len(today) != 10:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        lyear = year % 4 # TODO: put this into the function leap_year.
        if lyear == 0:
            feb_max = 29 # this is a leap year
        else:
            feb_max = 28 # this is not a leap year

        lyear = year % 100
        if lyear == 0:
            feb_max = 28 # this is not a leap year

        lyear = year % 400
        if lyear == 0:
            feb_max = 29 # this is a leap year

        tmp_day = day + 1 # next day

        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if tmp_day > mon_max[month]:
            to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
            tmp_month = month + 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month > 12:
            to_month = 1
            year = year + 1
        else:
            to_month = tmp_month + 0

        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return next_date

def before():
    "TODO enter docstring."
    pass # TODO replace this with code, using your algorithm document.

def dbda(start_date, num_days):
    end_date = 0
    # create a loop
    # call before() or after() as appropriate
    # return end_date

if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    # output the result
    pass
