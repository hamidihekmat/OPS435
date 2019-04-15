# OPS435 Assignments  (Winter Term of 2019)

All the assignment for OPS435, class of 2019

# Assignment 1
This program was written with python using the built in function. OS module was not used.
# USAGE
Usage: Date_Predictor.py (YYYYMMDD) +/-Day

e.g. -> 20190101 +1 = 20190102



*Using --step parameter*
[./Date_Predictor.py --step (YYYYMMDD) +/- Days]
e.g. -> [./Date_Predictor.py --step 20190101 5]
-> 20190102
-> 20190103
-> 20190104
-> 20190105
-> 20190106

*Calculate the # of days*

[./Date_Predictor.py (YYYYMMDD) (YYYYMMDD)
e.g. -> [./a1_hwhamidi.py 19960101 19970101]
-> 366'''

# Argparser Usage Data For User/Rhost Assignment 2

# Usage

usage: ur_hwhamidi.py [-h] [-l {user,host}] [-r RHOST]
                      [-t {daily,weekly,monthly}] [-u USER] [-v]
                      F [F ...]

Usage Report based on the last command

positional arguments:
  F                     list of files to be processed

optional arguments:
  -h, --help            show this help message and exit
  -l {user,host}, --list {user,host}
                        generate user name or remote host IP from the given
                        files
  -r RHOST, --rhost RHOST
                        usage report for the given remote host IP
  -t {daily,weekly,monthly}, --type {daily,weekly,monthly}
                        type of report: daily, weekly, and monthly
  -u USER, --user USER  usage report for the given user name
  -v, --verbose         tune on output verbosity



