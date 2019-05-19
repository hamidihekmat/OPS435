#!/usr/bin/env python3

"""
Name: CheckLab2.py
Author: Andrew Oatley-Willis
Date: November 2, 2016

Usage:
hheck all sections for the labs
./CheckLab2-1 -f -v 
Check a specific lab section
./CheckLab2-1 -f -v lab2x 

Description:
This script is used to give students more feedback, progress, and
assistance while working on labs. Labs and this script should be 
in the same directory. Labs must use the correct naming scheme for
each file(eg. lab2a.py, lab2b.py, ...).


"""

import subprocess
import unittest
import sys
import os
import hashlib
import urllib.request

#~ class lab2a(unittest.TestCase):
    #~ """All test cases for lab2a - variables & printing"""

    #~ def test_0(self):
        #~ """[Lab 2] - [Investigation 1] - [Part 1] - variables & printing - Test for file creation: ./lab2a.py"""
        #~ error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        #~ self.assertTrue(os.path.exists('./lab2a.py'), msg=error_output)
    
    #~ def test_a(self):
        #~ """[Lab 2] - [Investigation 1] - [Part 1] - variables & printing - Test for errors running: ./lab2a.py"""
        #~ # Run students program
        #~ p = subprocess.Popen(['/usr/bin/python3', './lab2a.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        #~ stdout, err = p.communicate()
        #~ # Fail test if process returns a no zero exit status
        #~ return_code = p.wait()
        #~ error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        #~ self.assertEqual(return_code, 0, msg=error_output)

    #~ def test_a1(self):
        #~ """[Lab 2] - [Investigation X] - [Part X] - variables & printing - Test for correct shebang line: ./lab2X.py"""
        #~ lab_file = open('./lab2a.py')
        #~ first_line = lab_file.readline()
        #~ lab_file.close()
        #~ error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        #~ self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)




    #~ def test_b(self):
        #~ """variables & printing - Test output for correct output "Hi Jon, you are 20 years old.": ./lab2a.py"""
        #~ # Run students program
        #~ p = subprocess.Popen(['/usr/bin/python3', './lab2a.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        #~ stdout, _ = p.communicate()
        #~ # Fail test if output is different from expected_output
        #~ expected_output = b'Hi Jon, you are 20 years old.\n'
        #~ error_output = 'output is not correct(HINT: pay attention to uppercase letters, spaces, and punctuation)'
        #~ self.assertEqual(stdout, expected_output, msg=error_output)
    

class lab2b(unittest.TestCase):
    """All test cases for lab2b - variables & printing & input"""
    
    def test_0(self):
        """[Lab 2] - [Investigation X] - [Part X] - variables & printing - Test for file creation: ./lab2b.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab2b.py'), msg=error_output)
   
    def test_a(self):
        """variables & printing & input - Test for errors with sending input "Jon" "20": ./lab2b.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate(input=b'Jon\n20\n')
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_a1(self):
        """[Lab 2] - [Investigation X] - [Part X] - variables & printing - Test for correct shebang line: ./lab2X.py"""
        lab_file = open('./lab2b.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)

    def test_b(self):
        """variables & printing & input - Test output with sending input "Jon" "20": ./lab2b.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate(input=b'Jon\n20\n')
        # Fail test if output is different from expected_output
        expected_output = b'Name: Age: Hi Jon, you are 20 years old.\n'
        error_output = 'output is not correct(HINT: pay attention to spelling, uppercase letters, spaces, and punctuation)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_c(self):
        """variables & printing & input - Test output with sending input "Jen" "25": ./lab2b.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate(input=b'Jen\n25\n')
        # Fail test if output is different from expected_output
        expected_output = b'Name: Age: Hi Jen, you are 25 years old.\n'
        error_output = 'output is not correct(HINT: we are matching "Jen" and "25" now, take a look at python function input()'
        self.assertEqual(stdout, expected_output, msg=error_output)
    

class lab2c(unittest.TestCase):
    """All test cases for lab2c - arguments"""
    
    def test_0(self):
        """[Lab 2] - [Investigation X] - [Part X] - variables & printing - Test for file creation: ./lab2X.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab2c.py'), msg=error_output)
    
    def test_a(self):
        """arguments - Test for errors with 2 args: ./lab2c.py Jon 20"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2c.py', 'Jon', '20' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual (return_code, 0, msg=error_output)
    
    def test_a1(self):
        """[Lab 2] - [Investigation X] - [Part X] - variables & printing - Test for correct shebang line: ./lab2X.py"""
        lab_file = open('./lab2c.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)

    def test_b(self):
        """arguments - Test output with 2 args: ./lab2c.py Jon 20"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2c.py', 'Jon', '20' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Hi Jon, you are 20 years old.\n'
        error_output = 'output is not correct(HINT: try using the sys.argv list, do not forget to import sys)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_c(self):
        """arguments - Test output with 2 different args: ./lab2c.py Jen 25"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2c.py', 'Jen', '25' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Hi Jen, you are 25 years old.\n'
        error_output = 'output is not correct(HINT: try using the sys.argv list, do not forget to import sys)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    

class lab2d(unittest.TestCase):
    """All test cases for lab2d - arguments & if statements"""
    
    def test_0(self):
        """[Lab 2] - [Investigation X] - [Part X] - variables & printing - Test for file creation: ./lab2X.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab2d.py'), msg=error_output)
    
    def test_a(self):
        """arguments & if statements - Test for errors with 0 args: ./lab2d.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2d.py' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_a1(self):
        """[Lab 2] - [Investigation X] - [Part X] - variables & printing - Test for correct shebang line: ./lab2X.py"""
        lab_file = open('./lab2d.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)
    
    def test_b(self):
        """arguments & if statements - Test for errors with 1 args: ./lab2d.py Jon"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2d.py', 'Jon' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_c(self):
        """arguments & if statements - Test for errors with 2 args: ./lab2d.py Jon 20"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2d.py', 'Jon', '20' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_d(self):
        """arguments & if statements - Test for errors with 3 args: ./lab2d.py Jon 20 More"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2d.py', 'Jon', '20', 'More' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_e(self):
        """arguments & if statements - Test output with 0 args: ./lab2d.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2d.py' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Usage: ./lab2d.py name age\n'
        error_output = 'wrong output for number of args(HINT: use if statements for catching conditions, such as 0 arguments)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_f(self):
        """arguments & if statements - Test output with 1 args: ./lab2d.py Jon"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2d.py', 'Jon' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Usage: ./lab2d.py name age\n'
        error_output = 'wrong output for number of args(HINT: use if and elif statements for catching conditions, such as 1 argument)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_g(self):
        """arguments & if statements - Test output with 2 args: ./lab2d.py Jon 20"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2d.py', 'Jon', '20' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Hi Jon, you are 20 years old.\n'
        error_output = 'wrong output for number of args'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_h(self):
        """arguments & if statements - Test output with 3 args: ./lab2d.py Jon 20 More"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2d.py', 'Jon', '20', 'More' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Usage: ./lab2d.py name age\n'
        error_output = 'wrong output for number of args(HINT: use the > or < signs in if statements, test for more then 2 arguments)'
        self.assertEqual(stdout, expected_output, msg=error_output)

class lab2e(unittest.TestCase):
    """All test cases for lab2e - while loops"""
    
    def test_0(self):
        """[Lab 2] - [Investigation X] - [Part X] - variables & printing - Test for file creation: ./lab2X.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab2e.py'), msg=error_output)

    def test_a(self):
        """while loops - Test for errors: ./lab2e.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2e.py' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_a1(self):
        """[Lab 2] - [Investigation X] - [Part X] - variables & printing - Test for correct shebang line: ./lab2X.py"""
        lab_file = open('./lab2e.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)

    def test_b(self):
        """while loops - Test output of while loop running 10 times: ./lab2e.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2e.py' ], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nblast off!\n'
        error_output = 'wrong output(HINT: pay attention to the last number that is displayed, is it a 1 or a 0?)'
        self.assertEqual(stdout, expected_output, msg=error_output)

class lab2f(unittest.TestCase):
    """All test cases for lab2f - while loops & arguments"""
    
    def test_0(self):
        """[Lab 2] - [Investigation X] - [Part X] - variables & printing - Test for file creation: ./lab2X.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab2f.py'), msg=error_output)

    def test_a(self):
        """while loops & arguments - Test for errors(WARNING: this script is NOT suppose to run with 0 arguments): ./lab2f.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2f.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = '(HINT: this script should only be run with a argument)'
        self.assertEqual(return_code, 1, msg=error_output)
    
    def test_a1(self):
        """[Lab 2] - [Investigation X] - [Part X] - variables & printing - Test for correct shebang line: ./lab2X.py"""
        lab_file = open('./lab2f.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)

    def test_b(self):
        """while loops & arguments - Test for errors: ./lab2f.py 10"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2f.py', '10'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error, careful not to mix up ints and strings)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_c(self):
        """while loops & arguments - Test for errors: ./lab2f.py 5"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2f.py', '5'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error, careful not to mix up ints and strings)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_d(self):
        """while loops & arguments - Test output of while loop running 10 times: ./lab2f.py 10"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2f.py', '10'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nblast off!\n'
        error_output = 'wrong output(HINT: )'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_e(self):
        """while loops & arguments - Test output of while loop running 5 times: ./lab2f.py 5"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2f.py', '5'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'5\n4\n3\n2\n1\nblast off!\n'
        error_output = 'wrong output(HINT: )'
        self.assertEqual(stdout, expected_output, msg=error_output)


class lab2g(unittest.TestCase):
    """All test cases for lab2g - while loops & arguments & if statements"""
    
    def test_0(self):
        """[Lab 2] - [Investigation X] - [Part X] - variables & printing - Test for file creation: ./lab2X.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab2g.py'), msg=error_output)

    def test_a(self):
        """while loops & arguments & if statements - Test for errors: ./lab2g.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2g.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_a1(self):
        """[Lab 2] - [Investigation X] - [Part X] - variables & printing - Test for correct shebang line: ./lab2X.py"""
        lab_file = open('./lab2g.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)
    
    def test_b(self):
        """while loops & arguments & if statements - Test for errors: ./lab2g.py 5"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2g.py', '5'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error, careful not to mix up ints and strings)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_c(self):
        """while loops & arguments & if statements - Test for errors: ./lab2g.py 10"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2g.py', '10'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error, careful not to mix up ints and strings)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_d(self):
        """while loops & arguments & if statements - Test output of while loop with no arguments: ./lab2g.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2g.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'3\n2\n1\nblast off!\n'
        error_output = 'wrong output(HINT: )'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_e(self):
        """while loops & arguments & if statements - Test output of while loop running 10 times: ./lab2g.py 5"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2g.py', '5'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'5\n4\n3\n2\n1\nblast off!\n'
        error_output = 'wrong output(HINT: )'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
    def test_f(self):
        """while loops & arguments & if statements - Test output of while loop running 10 times: ./lab2g.py 10"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab2g.py', '10'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nblast off!\n'
        error_output = 'wrong output(HINT: )'
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
        lab_name = 'CheckLab2.py'
        lab_num = 'lab2'
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


