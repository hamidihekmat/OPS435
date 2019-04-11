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

Copyright 2019 - Hekmat Hamidi
