#!/usr/bin/env python3

import argparse
import os
import time

'''
OPS435 Assignment 2 - Winter 2019
Program: ur_hwhamidi.py
Author: "Hekmat Hamidi"
The python code in this file ur_hwhamidi.py is original work written by
"Hekmat Hamidi". No code in this file is copied from any other source 
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and violators 
will be reported and appropriate action will be taken.'''

#Warning Messages
WARNING = '\033[91m'
ENDC = '\033[0m'






def host_user(file_list):
    '''
    Description
    -----------
    Parses all hosts/users from a given usage data file.

    Parameters
    ----------
    file_list: list
        all the records in usage data file
        
    Returns
    string
        all unique hosts 

    Examples
    -------
    1. user report
        [rchan@centos7 a2]$ ./ur_hwhamidi.py -l user usage_data_file
        User list for usage_data_file
        =============================
        asmith
        bigia
        cwsmith
        hfang
        mlee18
        mshana
        rchan
        tsliu2
    
    2. host report
        [rchan@centos7 a2]$ ./ur.py -l host usage_data_file
        Host list for usage_data_file
        =============================
        10.40.105.130
        10.40.43.94
        10.40.91.236
        10.40.91.247
        10.43.115.162
        24.114.50.50


    Raises
    ------
    TypeError
        when required positional arguments are not given''' 
    string_user = "Host list for"
    for file in range(len(args.F)):
        string_user += (" " + args.F[file])
    print(string_user)
    print("=" * len(string_user))
    list_host = []
    list_user = []
    if args.list == "host":
        for line in file_list:
            host_in_list = line.split()
            hosts = host_in_list[2]
            list_host.append(hosts)
        #removes duplicates of hosts
        set_host = set(list_host)
        for host in sorted(set_host):
            print(host)
    if args.list == "user":
        for line in file_list:
            user_in_list = line.split()
            users = user_in_list[0]
            list_user.append(users)
        #renoves deplicates for users
        set_user = set(list_user)
        for user in sorted(set_user):
            print(user)

def daily(logout,login):
    '''
    Description
    -----------
    Computes the differnce in seconds for logout and login logs for given user.

    Parameters
    ----------
    logout: list
        list of logout logs in asctime format e.g -> [Tue April 5 23:34:44 2019]
    login: list
        list of login logs in asctime format e.g -> [Tue April 5 22:34:44 2019]

    Returns
    string
        daily records for given user/host in seconds and displays it in ordered fashion

    Examples
    --------
    1. daily usage report by user 
        [rchan@centos7 a2]$ ./ur.py -u rchan -t daily usage_data_file
        Daily Usage Report for rchan
        ============================
        Date          Usage in Seconds
        2018 02 13        1580
        Total             1580

    2. daily usage report by remote host
        [rchan@centos7 a2]$ ./ur.py -r 10.40.105.130 -t daily usage_data_file
        Daily Usage Report for 10.40.105.130
        ====================================
        Date          Usage in Seconds
        2018 02 13        7969
        Total             7969

    Raises
    ------
    TypeError
        when required positional arguments are not given''' 

    list_key = []
    list_value = []
    records_all = {}
# calculate the total of seconds 
    for logout,login in zip(logout,login):
        # if the date are the same in login and logout records
        #if logout[:10] == login[:10]:
        time_diff = time.mktime(time.strptime(logout)) - time.mktime(time.strptime(login))
        tmp_date = (time.strptime(logout))
        date = time.strftime("%Y %m %d", tmp_date)

        try:
            records_all[date] += time_diff
        except:
            records_all[date] = time_diff
            
    total_seconds = 0
    if args.rhost:
        host_user = args.rhost
    else:
        host_user = args.user
    string_daily = "Daily Usage Report for " + str(host_user)
    print(string_daily)
    print("=" * len(string_daily))
    print("Date        Usage in Seconds")
    for dates,seconds in sorted(records_all.items(), reverse=True):
        print(str(dates) + "         " + str(int(seconds)))
        total_seconds += seconds
    print("Total" + "              " + str(int(total_seconds)))





def weekly(logout,login):
    '''
    Description
    -----------
    Computes the differnce in seconds for logout and login logs for given user.

    Parameters
    ----------
    logout: list
        list of logout logs in asctime format e.g -> Tue April 5 22:34:44 2019
    login: list
        list of login logs in asctime format e.g -> Tue April 5 22:34:44 2019

    Returns
    string
        weekly records for given user/host in seconds and displays it in ordered fashion

    Examples
    --------
    
    1. weekly usage report by user
        [rchan@centos7 a2]$ ./ur.py -u rchan -t weekly usage_data_file
        Weekly Usage Report for rchan
        =============================
        Week #        Usage in Seconds
        2018 07           1580
        Total             1580

    2. weekly usage report by remote host
        [rchan@centos7 a2]$ ./ur.py -r 10.40.105.130 -t daily usage_data_file
        Daily Usage Report for 10.40.105.130
        ====================================
        Date          Usage in Seconds
        2018 02 13        7969
        Total             7969


    Raises
    ------
    TypeError
        when required positional arguments are not given''' 
    list_key = []
    list_value = []
    records_all = {}
#calculate the total of seconds 
    for logout,login in zip(logout,login):
        # if the date are the same in login and logout records
        #if logout[:10] == login[:10]:
        time_diff = time.mktime(time.strptime(logout)) - time.mktime(time.strptime(login))
        tmp_date = (time.strptime(logout, "%a %b %d %H:%M:%S %Y"))
        date = time.strftime("%Y %W", tmp_date)

        try:
            records_all[date] += time_diff
        except:
            records_all[date] = time_diff
           
    total_seconds = 0
    if args.rhost:
        host_user = args.rhost
    else:
        host_user = args.user
    string_weekly = "Weekly Usage Report for " + str(host_user)
    print(string_weekly)
    print("=" * len(string_weekly))

    print("Week #       Usage in Seconds")
    for dates,seconds in sorted(records_all.items(), reverse=True):
        print(str(dates) + "            " + str(int(seconds)))
        total_seconds += seconds
    print("Total" + "              " + str(int(total_seconds)))

def monthly(logout,login):
    '''
    Description
    -----------
    Computes the differnce in seconds for logout and login logs for given user.

    Parameters
    ----------
    logout: list
        list of logout logs in asctime format e.g -> [Tue April 5 22:34:44 2019]
    login: list
        list of login logs in asctime format e.g -> [Tue April 5 22:34:44 2019]

    Returns
    string
        montly records for given user/host in seconds and displays it in ordered fashion

    Examples
    --------
    1. monthly usage report by user
        [rchan@centos7 a2-2018fall]$ ./ur.py -u rchan -t monthly usage_data_file
        Monthly Usage Report for rchan
        ==============================
        Month         Usage in Seconds
        2018 02           1580
        Total             1580
    
    2. monthly usage report by remote host
        [rchan@centos7 a2-2018fall]$ ./ur.py -r 10.40.105.130 -t monthly usage_data_file
        Monthly Usage Report for 10.40.105.130
        ======================================
        Month         Usage in Seconds
        2018 02           7969
        Total             7969

    Raises
    ------
    TypeError
        when required positional arguments are not given''' 
    list_key = []
    list_value = []
    records_all = {}
#calculate the total of seconds 
    for logout,login in zip(logout,login):
        # if the date are the same in login and logout records
        #if logout[:10] == login[:10]:
        time_diff = time.mktime(time.strptime(logout)) - time.mktime(time.strptime(login))
        tmp_date = (time.strptime(logout, "%a %b %d %H:%M:%S %Y"))
        date = time.strftime("%Y %m", tmp_date)

        try:
            records_all[date] += time_diff
        except:
            records_all[date] = time_diff
          
    total_seconds = 0
    if args.rhost:
        host_user = args.rhost
    else:
        host_user = args.user
    string_monthly = "Monthly Usage Report for " + str(host_user)
    print(string_monthly)
    print("=" * len(string_monthly))
    print("Month         Usage in Seconds")
    for dates,seconds in sorted(records_all.items()):
        print(str(dates) + "            " + str(int(seconds)))
        total_seconds += seconds
    print("Total" + "              " + str(int(total_seconds)))

def create_logs(records):
    '''
    Description
    -----------
    Creates login/logout logs for given records.

    Parameters
    ----------
    records: list
        list of records for given user/host

    Returns
    -------
    new_outs: list
        list of logout logs for the given records for a user/host in asctime format e.g -> [Tue April 5 22:34:44 2019]
    new_logs: list
        list of login logs for the given records for a user/host in asctime format e.g -> [Tue April 5 23:34:44 2019]

    Raises
    -------
    TypeError
        when required positional arguments are not given'''
    space = " "
    logs = []
    outs = []
    new_logs = []
    new_outs = []
    data_records = records
    for line in data_records:
        date_log = line[3:8]
        date_out = line[9:14]

        logs.append(space.join(date_log))
        outs.append(space.join(date_out))

    #testing the perfect algorithm
    for out,log in zip(outs, logs):
        tmp_out = time.strptime(out)
        tmp_log = time.strptime(log)
        format_out = time.strftime("%Y %m %d", tmp_out)
        format_log = time.strftime("%Y %m %d", tmp_log)
        if out[:10] == log[:10]:
            new_outs.append(out)
            new_logs.append(log)

        if format_out != format_log:
            new_logs.append(log)
            new_outs.append(log[:10] + " 23:59:59 " + log[19:26])
            sec_tomorrow = time.mktime(time.strptime(format_log, "%Y %m %d"))
            string_tomorrow = time.ctime(sec_tomorrow + 86400 ) #-> returns string time e.g (TUE FEB 14 00:00:00 2019)
            tuple_tomorrow = time.strptime(string_tomorrow) #-> returns tupule time format
            tomorrow = time.strftime("%Y %m %d", tuple_tomorrow) # > 2018 02 14 and 
            if tomorrow == format_out:
                new_outs.append(out)
                new_logs.append(string_tomorrow)
            while tomorrow != format_out:
                l_tomorrow = time.mktime(time.strptime(tomorrow, "%Y %m %d"))
                l_string = time.ctime(l_tomorrow)
                new_logs.append(l_string)

                new_outs.append(l_string[:10] + " 23:59:59 " + l_string[20:26])
                tmp_tomorrow = time.mktime(time.strptime(tomorrow, "%Y %m %d"))
                tmp_string = time.ctime(tmp_tomorrow + 86400)
                tupule = time.strptime(tmp_string)
                tomorrow = time.strftime("%Y %m %d", tupule)

                if tomorrow == format_out:
                    new_outs.append(tmp_string[:3] + out[3:])
    
                    new_logs.append(tmp_string)

    #if choice == "daily" calll daily
    if args.type == "daily":
        daily(new_outs, new_logs)
    if args.type == "weekly":
        weekly(new_outs, new_logs)
    if args.type == "monthly":
        monthly(new_outs, new_logs)
        
def create_records(file_list):
    '''
    Description
    -----------
    Creates records for given user or host.

    Parameters
    ----------
    host_user : string
        username or host for given file
    file_list: list
        list of records for usage data file

    Returns
    -------
    list
        a list of records for given user or host

    Raises
    ------
    TypeError
        when required positional arguments are not given'''


    data_list = []
    data_records = []
    for line in file_list:
        lines = line.split()
        data_list.append(lines)
    if args.user:
        user = args.user
        for record in data_list:
            if user == record[0]:
                data_records.append(record)
                
                

    if args.rhost:
        host = args.rhost
        for record in data_list:
            if host == record[2]:
                data_records.append(record)

    create_logs(data_records)

def verbosity():
        '''
        Description
        -----------
        Verbosity is an option for producing detailed logging information.

        Returns
        -------
        string
            detailed logging information

        Example
        -------
        + ./ur.py -u user5 -t monthly a2_test_data_2 -v
        Files to be processed: ['a2_test_data_2']
        Type of args for files <class 'list'>
        usage report for user: user5
        usage report type: monthly
        processing usage report for the following:
        reading login/logout record files ['a2_test_data_2']
        Monthly Usage Report for user5
        '''
        print("Files to be processed:", args.F)
        print("Type of args for files", type(args.F))
        if args.user:
            print("usage report for user:", args.user)
        if args.rhost:
            print("usage report for remote host:", args.rhost)

        if args.type:
            print("usage report type:", args.type)
        print("processing usage report for the following:")
        print("reading login/logout record files", args.F)

def Main():
    ''' 
    Description
    -----------
    Main function contains relevant parser arguments for command-line interface


    Positional Arguments
    ---------------------
    F                     list of files to be processed


    Optional Arguments:
    -------------------
    h--list, --help            show this help message and exit

    -l {user,host}, --list {user,host}
                        generate user name or remote host IP from the given
                        files
    -r RHOST, --rhost RHOST
                        usage report for the given remote host IP
    -t {daily,weekly,monthly}, --type {daily,weekly,monthly}
                        type of report: daily, weekly, and monthly
    -u USER, --user USER  usage report for the given user name
    -v, --verbose         tune on output verbosity

    '''
    global parser
    global args

    parser = argparse.ArgumentParser(epilog="Copyright 2019 - Hekmat Hamidi", description="Usage Report based on the last command")
    #argument options for commandline
    parser.add_argument("-l","--list", choices=("user","host"), help="generate user name or remote host IP from the given files")
    parser.add_argument("-r","--rhost", help="usage report for the given remote host IP")
    parser.add_argument("-t","--type", choices=("daily","weekly","monthly"), help="type of report: daily, weekly, and monthly")
    parser.add_argument("-u","--user", help="usage report for the given user name")
    parser.add_argument("-v", "--verbose", action="store_true", help="tune on output verbosity")
    parser.add_argument("F", nargs="+", help="list of files to be processed")


    args = parser.parse_args()
    #the lines of each filelist provided will be extended (added) to the emply file_list
    file_list = []
    #set file_list to to given file from command line args
    
    for file in args.F:
        if file.upper() == "LAST":
            os.system("last -Fwi | grep pts > last")
            f = open("last", "r")
            last = f.readlines()
            for line in last:
                tmp_line = line.split()
                if len(tmp_line) == 15:
                    record = ' '.join(tmp_line)
                    file_list.append(record)
            f.close()
        else:

            try: 
                tmp_file = open(file, 'r')
                tmp_read = tmp_file.readlines()
                file_list.extend(tmp_read)
                tmp_file.close()
            except:
                print( WARNING + "!!! > Please Check the filename < !!!" + ENDC)
                os.system("ls")
                exit()

    #list option
    if args.list:
        if args.verbose:
            verbosity()
            host_user(file_list)
        else:
            host_user(file_list)




    #usage report option
    if args.user or args.rhost:
        if args.type:
            if args.verbose:
                verbosity()
                create_records(file_list)
            else:
                create_records(file_list)

if __name__ == "__main__":
    Main()
