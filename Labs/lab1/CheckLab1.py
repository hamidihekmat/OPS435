#!/usr/bin/env python3

"""
Name: CheckLab1.py
Author: Andrew Oatley-Willis
Date: November 2, 2016

Usage:
Check all sections for the labs
./CheckLab1-1 -f -v 
Check a specific lab section
./CheckLab1-1 -f -v lab1x 

Description:
This script is used to give students more feedback, progress, and
assistance while working on labs. Labs and this script should be 
in the same directory. Labs must use the correct naming scheme for
each file(eg. lab1a.py, lab1b.py, ...).


"""
from __future__ import absolute_import, division, print_function, unicode_literals
import subprocess
import unittest
import sys
import os
import hashlib
import urllib.request
import socket 
    
class lab0a(unittest.TestCase):
    """All test cases for lab0a - making sure the install has correct configuration"""
    
    def test_a(self):
        """[Lab 1] - [Investigation 1] - [Part 1] - installing linux - supported linux distribution"""
        # dist, release, version = platform.linux_distribution() # Deprecated in python
        # Suggested to use the os-release file for distribution version
        try:
            f = open('/etc/os-release', 'r')
            dat = f.readlines()
            f.close()
            dist = dat[2][3:].strip().strip('"') # Grab the standard location for dist id
        except:
            dist = 'unknown'
        error_output = 'your system must be centos'
        self.assertEqual(dist, 'centos', msg=error_output)
    
    def test_b(self):
        """[Lab 1] - [Investigation 1] - [Part 1] - installing linux - disk/partition sizes"""
        self.assertEqual(1, 1, msg='place holder')
    
    def test_c(self):
        """[Lab 1] - [Investigation 1] - [Part 1] - installing linux - correct hostname"""
        hostname = socket.gethostname()
        self.assertEqual(hostname, 'centos7', msg='place holder')

class lab0b(unittest.TestCase):
    """All test cases for lab0b - installing software"""

    def test_a(self):
        """[Lab 1] - [Investigation 1] - [Part 2] - additional software - software packages installed"""
        #import rpm
        # Create objects to make a rpm query
        #transaction = rpm.TransactionSet()
        #match = transaction.dbMatch()
        p = subprocess.Popen(['/usr/bin/rpm', '-qa', '--qf', '%{NAME}\n'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        match = stdout.decode('utf-8').split()

        # List of packages to check if installed
        packages = ['python34', 'python', 'screen', 'tmux', 'vim-common', 'vim-enhanced', 'python2-pip', 'python34-pip', 'python-ipython'] 
        installedpackages = []
        # Compare all installed rpms with above list
        for package in match:
            # rpm returns bytes instead of characters, decode them to strings
            #name = package['name'].decode('UTF-8')
            name = package
            #version = package['version'].decode('UTF-8')
            #release = package['release'].decode('UTF-8')
            if name in packages:
                installedpackages.append(name)
        # Find missing packages from packages list
        diff = list(set(packages).symmetric_difference(installedpackages))
        error_output = 'your system may be missing software required to move to the next step', diff
        self.assertEqual(diff, [], msg=error_output)
        
        
        
    def test_b(self):
        """[Lab 1] - [Investigation 1] - [Part 2] - additional software - pip install software"""
        p = subprocess.Popen(['pip3', 'list'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        match = stdout.decode('utf-8').split('\n')

        # List of packages to check if installed
        packages = ['ipython']
        installedpackages = []
        for package in match:
            # Extract package name and delete extra items
            packagename = package.split() 
            if packagename != []:
                if packagename[0] in packages:
                    installedpackages.append(packagename[0])
        # Find missing packages from packages list
        diff = list(set(packages).symmetric_difference(installedpackages))
        error_output = 'your system may be missing software required to move to the next step', diff
        self.assertEqual(diff, [], msg=error_output)
    
    def test_c(self):
        """[Lab 1] - [Investigation 1] - [Part 3] - additional software - all text editors installed"""
        self.assertEqual(1, 1, msg='not currently requiring all text editors to be installed')

class lab0c(unittest.TestCase):
    """All test cases for lab0c - ipython alias and confirguration"""
    
    def test_b(self):
        """[Lab 1] - [Investigation 2] - [Part 1] - ipython - ipython configuration"""
        self.assertEqual(1, 1, msg='place holder')
    
    def test_c(self):
        """[Lab 1] - [Investigation 2] - [Part 1] - directories - Test for directory structure creation"""
        dirs_required = ['~/ops435/lab1', 
                                '~/ops435/lab2',
                                '~/ops435/lab3',
                                '~/ops435/lab4',
                                '~/ops435/lab5',
                                '~/ops435/lab6',
                                '~/ops435/lab7',
                                '~/ops435/lab8']
        dirs_exist = True
        for d in dirs_required:
            if not os.path.isdir(os.path.expanduser(d)):
                dirs_exist = False
        error_output = 'your directory cannot be found(HINT: make sure you have created all the required directories)', dirs_required
        self.assertTrue(dirs_exist, msg=error_output)


class lab1a(unittest.TestCase):
    """All test cases for lab1a - printing"""
    
    def test_0(self):
        """[Lab 1] - [Investigation 3] - [Part 2] - printing - Test for file creation: ./lab1a.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab1a.py'), msg=error_output)
        

    def test_a(self):
        """[Lab 1] - [Investigation 3] - [Part 2] - printing - Test for errors running: ./lab1a.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1a.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see/read the error)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 1] - [Investigation 3] - [Part 2] - printing - Test for correct shebang line: ./lab1a.py"""
        lab_file = open('./lab1a.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line, '#!/usr/bin/env python3\n', msg=error_output)


    def test_b(self):
        """[Lab 1] - [Investigation 3] - [Part 2] - printing - Test output for correct output "Hello world": ./lab1a.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1a.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Hello world\n'
        error_output = 'output is not correct(HINT: pay attention to uppercase letters, spaces, and symbols)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
class lab1b(unittest.TestCase):
    """All test cases for lab1b - variables & printing"""
   
    def test_0(self):
        """[Lab 1] - [Investigation 3] - [Part 3] - variables & printing - Test for file creation: ./lab1b.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue( os.path.exists('./lab1b.py'), msg=error_output)

    def test_a(self):
        """[Lab 1] - [Investigation 3] - [Part 3] - variables & printing - Test for errors running: ./lab1b.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_a1(self):
        """[Lab 1] - [Investigation 3] - [Part 3] - variables & printing - Test for correct shebang line: ./lab1b.py"""
        lab_file = open('./lab1b.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line, '#!/usr/bin/env python3\n', msg=error_output)

    def test_b(self):
        """[Lab 1] - [Investigation 3] - [Part 3] - variables & printing - Test for correct output "How old are you Isaac?": ./lab1b.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'How old are you Isaac?\n'
        error_output = 'output is not correct(HINT: pay attention to uppercase letters, spaces, and punctuation)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    

class lab1c(unittest.TestCase):
    """All test cases for lab1c - variables & printing"""
    
    def test_0(self):
        """[Lab 1] - [Investigation 3] - [Part 4] - variables & printing - Test for file creation: ./lab1c.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue( os.path.exists('./lab1c.py'), msg=error_output)

    def test_a(self):
        """[Lab 1] - [Investigation 3] - [Part 4] - variables & printing - Test for errors running: ./lab1c.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1c.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_a1(self):
        """[Lab 1] - [Investigation 3] - [Part 4] - variables & printing - Test for correct shebang line: ./lab1c.py"""
        lab_file = open('./lab1c.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line, '#!/usr/bin/env python3\n', msg=error_output)

    def test_b(self):
        """[Lab 1] - [Investigation 3] - [Part 4] - variables & printing - Test output for correct output "Isaac is 72 years old!": ./lab1c.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1c.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Isaac is 72 years old!\n'
        error_output = 'output is not correct(HINT: pay attention to uppercase letters, spaces, and punctuation)'
        self.assertEqual(stdout, expected_output, msg=error_output)

class lab1d(unittest.TestCase):
    """All test cases for lab1d - Math Operators"""
    
    def test_0(self):
        """[Lab 1] - [Investigation 3] - [Part 5] - math operators - Test for file creation: ./lab1d.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue( os.path.exists('./lab1d.py'), msg=error_output)

    def test_a(self):
        """[Lab 1] - [Investigation 3] - [Part 5] - math operators - Test for errors running: ./lab1d.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1d.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_a1(self):
        """[Lab 1] - [Investigation 3] - [Part 5] - math operators - Test for correct shebang line: ./lab1d.py"""
        lab_file = open('./lab1d.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line, '#!/usr/bin/env python3\n', msg=error_output)

    def test_b(self):
        """[Lab 1] - [Investigation 3] - [Part 5] - math operators - Test output for correct output "10 + 2 * 5 = 20": ./lab1d.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1d.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'10 + 2 * 5 = 20\n'
        error_output = 'output is not correct(HINT: the program must have the exact output, this includes every space and symbol)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
   
def ChecksumLatest(url=None):
    dat = ''
    with urllib.request.urlopen(url) as response:
        for line in response:
            line = line.decode('utf-8')
            dat = dat + line
    checksum = hashlib.sha256(dat.encode('utf-8')).digest()
    #print("internet", checksum)
    return checksum

def ChecksumLocal(filename=None):
    fil = open(filename, 'r', encoding='utf-8')
    dat = fil.readlines()
    textdata = ''
    for line in dat:
        textdata = textdata + line
    checksum = hashlib.sha256(textdata.encode('utf-8')).digest()
    #print("local", checksum)
    return checksum

def CheckForUpdates():
    try:
        lab_name = 'CheckLab1.py'
        lab_num = 'lab1'
        print('Checking for updates...')
        if ChecksumLatest(url='https://raw.githubusercontent.com/Seneca-CDOT/ops435/master/LabCheckScripts/' + lab_name) != ChecksumLocal(filename='./' + lab_name):
            print()
            print(' There is a update available for this' + lab_name + ' please consider updating:')
            print(' cd ~/ops435/' + lab_num + '/')
            print(' pwd  #   <-- i.e. confirm that you are in the correct directory')
            print(' rm ' + lab_name)
            print(' ls ' + lab_name + ' || wget https://raw.githubusercontent.com/Seneca-CDOT/ops435/master/LabCheckScripts/' + lab_name)
            print()
            return
        print('Running latest version...')
        return
    except:
        # Cleanly skip updating if any errors occur for offline or matrix issues
        print('No connection made...')
        print('Skipping updates...')
        return


if __name__ == '__main__':
    CheckForUpdates()
    wait = input('Press ENTER to run the Lab Check...')
    unittest.main()














