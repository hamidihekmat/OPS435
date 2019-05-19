#!/usr/bin/env python3

import subprocess
import unittest
import sys
import os
import hashlib
import urllib.request

#Import student files, do not give errors if they don't exist
#try:
#    import lab3b as lab3bStudent
#except:
#    """Could not find lab3b.py"""
##try:
#    import lab3c as lab3cStudent
#except:
#    """Could not find lab3c.py"""

class lab3a(unittest.TestCase):
    """All test cases for lab3b - functions & arguments"""

    def test_0(self):
        """[Lab 3] - [Investigation 1] - [Part 1] - Functions - Test for file creation: ./lab3a.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab3a.py'), msg=error_output)

    def test_a(self):
        """[Lab 3] - [Investigation 1] - [Part 1] - Functions - Test for errors running: ./lab3a.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab3a.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 3] - [Investigation 1] - [Part 1] - Functions - Test for correct shebang line: ./lab3a.py"""
        lab_file = open('./lab3a.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)
    

    def test_b_function_return_text_value(self):
        """[Lab 3] - [Investigation 1] - [Part 1] - Functions - function print_out_text() has correct output"""
        # Try to import before testing
        try:
            import lab3a as lab3aStudent
        except:
            self.fail('lab3a.py contains errors(HINT: make sure you copied the script exactly!')
        expected_output = 'Good Morning Terry'
        error_output = 'lab3a.py print_out_text() has wrong output(HINT: make sure you copied the script exactly!'
        self.assertEqual(lab3aStudent.return_text_value(), expected_output, msg=error_output)
    
    def test_c_function_return_number_value(self):
        """[Lab 3] - [Investigation 1] - [Part 1] - Functions - function print_out_text() has correct output"""
        # Try to import before testing
        try:
            import lab3a as lab3aStudent
        except:
            self.fail('lab3a.py contains errors(HINT: make sure you copied the script exactly!')
        expected_output = 15
        error_output = 'lab3a.py print_out_text() has wrong output(HINT: make sure you copied the script exactly!'
        self.assertEqual(lab3aStudent.return_number_value(), expected_output, msg=error_output)


class lab3b(unittest.TestCase):
    """All test cases for lab3b - functions & arguments"""

    def test_0(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - Functions - Test for file creation: ./lab3b.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab3b.py'), msg=error_output)

    def test_a(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - Functions - Test for errors running: ./lab3b.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab3b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a_function_sum(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments - function sum_numbers() fails without 2 arguments"""
        with self.assertRaises(Exception) as context:
            import lab3b as lab3bStudent
            lab3bStudent.sum_numbers()

    def test_a1(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - Functions - Test for correct shebang line: ./lab3b.py"""
        lab_file = open('./lab3b.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)


    def test_b_function_subtract(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments - function subtract_numbers() fails without 2 arguments"""
        with self.assertRaises(Exception) as context:
            import lab3b as lab3bStudent
            lab3bStudent.subtract_numbers()

    def test_c_function_multiply(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments - function multiply_numbers() fails without 2 arguments"""
        with self.assertRaises(Exception) as context:
            import lab3b as lab3bStudent
            lab3bStudent.multiply_numbers()

    def test_d_function_sum_output(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments - function add_numbers() adds correctly"""
        # Try to import before testing
        try:
            import lab3b as lab3bStudent
        except:
            self.fail('lab3b.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem adding(HINT: sum_numbers(10, 5)'
        self.assertEqual(str(lab3bStudent.sum_numbers(10, 5)), '15', msg=error_output)

    def test_e_function_subtract_output(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments - function subtract_numbers() subtracts correctly"""
        # Try to import before testing
        try:
            import lab3b as lab3bStudent
        except:
            self.fail('lab3b.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem subtracting(HINT: subtract_numbers(10, 5)'
        self.assertEqual(str(lab3bStudent.subtract_numbers(10, 5)), '5', msg=error_output)

    def test_f_function_multiply_output(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments - function multiply_numbers() multiplies correctly"""
        # Try to import before testing
        try:
            import lab3b as lab3bStudent
        except:
            self.fail('lab3b.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem multiplying(HINT: multiply_numbers(10, 5)'
        self.assertEqual(str(lab3bStudent.multiply_numbers(10, 5)), '50', msg=error_output)

class lab3c(unittest.TestCase):
    """All test cases for lab3c - functions & arguments & logic"""
    
    def test_0(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - Functions - Test for file creation: ./lab3c.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab3c.py'), msg=error_output)

    def test_a(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - Functions - Test for errors running: ./lab3c.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab3c.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)


    def test_a_function_sum(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments & logic - function operate() fails with 0 arguments"""
        with self.assertRaises(Exception) as context:
            lab3cStudent.operate()
    
    def test_a1(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - Functions - Test for correct shebang line: ./lab3X.py"""
        lab_file = open('./lab3c.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)


    def test_b_function_subtract(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments & logic - function operate() fails with 1 arguments"""
        with self.assertRaises(Exception) as context:
            lab3cStudent.operate(10)

    def test_c_function_multiply(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments & logic - function operate() fails with 2 arguments"""
        with self.assertRaises(Exception) as context:
            lab3cStudent.operate(10, 5)

    def test_d_function_sum_output(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments & logic - function operate() adds correctly test 1"""
        # Try to import before testing
        try:
            import lab3c as lab3cStudent
        except:
            self.fail('lab3c.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem adding(HINT: operate(10, 5, \'add\')'
        self.assertEqual(str(lab3cStudent.operate(10, 5, 'add')), '15', msg=error_output)

    def test_e_function_subtract_output(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments & logic - function operate() subtracts correctly test 1"""
        # Try to import before testing
        try:
            import lab3c as lab3cStudent
        except:
            self.fail('lab3c.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem subtracting(HINT: operate(10, 5, \'subtract\')'
        self.assertEqual(str(lab3cStudent.operate(10, 5, 'subtract')), '5', msg=error_output)

    def test_f_function_multiply_output(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments & logic - function operate() multiplies correctly test 1"""
        # Try to import before testing
        try:
            import lab3c as lab3cStudent
        except:
            self.fail('lab3c.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem multiplying(HINT: operate(10, 5, \'multiply\')'
        self.assertEqual(str(lab3cStudent.operate(10, 5, 'multiply')), '50', msg=error_output)
    
    def test_g_function_sum_output(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments & logic - function operate() adds correctly test 2"""
        # Try to import before testing
        try:
            import lab3c as lab3cStudent
        except:
            self.fail('lab3c.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem adding(HINT: operate(5, 50, \'add\')'
        self.assertEqual(str(lab3cStudent.operate(5, 50, 'add')), '55', msg=error_output)

    def test_h_function_subtract_output(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments & logic - function operate() subtracts correctly test 2"""
        # Try to import before testing
        try:
            import lab3c as lab3cStudent
        except:
            self.fail('lab3c.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem subtracting(HINT: operate(5, 50, \'subtract\')'
        self.assertEqual(str(lab3cStudent.operate(5, 50, 'subtract')), '-45', msg=error_output)

    def test_i_function_multiply_output(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments & logic - function operate() multiplies correctly test 2"""
        # Try to import before testing
        try:
            import lab3c as lab3cStudent
        except:
            self.fail('lab3c.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem multiplying(HINT: operate(5, 50, \'multiply\')'
        self.assertEqual(str(lab3cStudent.operate(5, 50, 'multiply')), '250', msg=error_output)
    
    def test_j_function_multiply_output(self):
        """[Lab 3] - [Investigation 2] - [Part 1] - functions & arguments & logic - function operate() fails with division"""
        # Try to import before testing
        try:
            import lab3c as lab3cStudent
        except:
            self.fail('lab3c.py contains errors(HINT: run the function and fix errors')
        error_output = 'function operate shows wrong output(HINT: the output must match exactly)'
        self.assertEqual(str(lab3cStudent.operate(5, 50, 'divide')), 'Error: function operator can be "add", "subtract", or "multiply"')
        

class lab3d(unittest.TestCase):
    """All test cases for lab3d - functions & subprocess"""
    
    def test_0(self):
        """[Lab 3] - [Investigation 2] - [Part 2] - Functions - Test for file creation: ./lab3d.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab3d.py'), msg=error_output)


    def test_a(self):
        """[Lab 3] - [Investigation 2] - [Part 2] - Functions - Test for errors running: ./lab3d.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab3d.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a_function_free_space(self):
        """[Lab 3] - [Investigation 2] - [Part 2] - functions & subprocess - Test function succeeds with 0 arguments"""
        # Try to import before testing
        try:
            import lab3d as lab3dStudent
        except:
            self.fail('lab3d.py contains errors(HINT: run the function and fix errors')
        # Test function
        try:
            lab3dStudent.free_space()
        except:
            self.fail('free_space() function contains errors(HINT: run the function and fix errors')
    
    def test_a1(self):
        """[Lab 3] - [Investigation 2] - [Part 2] - Functions - Test for correct shebang line: ./lab3d.py"""
        lab_file = open('./lab3d.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)

    
    def test_b_function_correct_output_free_space(self):
        """[Lab 3] - [Investigation 2] - [Part 2] - functions & subprocess - Test output shows free space of root"""
        # Try to import before testing
        try:
            import lab3d as lab3dStudent
        except:
            self.fail('lab3d.py contains errors(HINT: run the function and fix errors')
        p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], 
                            stdout=subprocess.PIPE, stdin=subprocess.PIPE, 
                            stderr=subprocess.PIPE, shell=True)
        stdout, err = p.communicate()
        try:
            error_output = 'wrong output(HINT: show root directory free space only)'
            self.assertEqual(stdout.decode('utf-8').strip(), 
                            lab3dStudent.free_space().decode('utf-8').strip(), msg=error_output)
        except AttributeError:
            error_output = 'did you already decode utf-8(HINT: you will need to do this later)'
            # If they already decoded the string an error will be raised this except fixes problem
            self.assertEqual(stdout.decode('utf-8').strip(), lab3dStudent.free_space().strip(), 
                            msg=error_output)
    
    def test_c_function_decode_free_space(self):
        """[Lab 3] - [Investigation 2] - [Part 2] - functions & subprocess - decode to utf-8 with string.decode('utf-8') successfully"""
        # Try to import before testing
        try:
            import lab3d as lab3dStudent
        except:
            self.fail('lab3d.py contains errors(HINT: run the function and fix errors')
        p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, err = p.communicate()
        error_output = 'output did not decode to utf-8(HINT: use string.decode(\'utf-8\') to decode)'
        # encode is used to turn unicode strings into bytes, decode turns bytes into unicode strings
        self.assertEqual(type(stdout.decode('utf-8')), type(lab3dStudent.free_space()), msg=error_output)

    def test_d_function_strip_free_space(self):
        """[Lab 3] - [Investigation 2] - [Part 2] - functions & subprocess - strip the new line character with string.strip() successfully """
        # Try to import before testing
        try:
            import lab3d as lab3dStudent
        except:
            self.fail('lab3d.py contains errors(HINT: run the function and fix errors')
        p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, err = p.communicate()
        error_output= 'output did not strip new line character(HINT: use string.strip() to remove)'
        self.assertNotEqual(stdout.decode('utf-8'), lab3dStudent.free_space(), msg=error_output)
    
class lab3e(unittest.TestCase):
    """All test cases for - functions & lists"""

    def test_0(self):
        """[Lab 3] - [Investigation 3] - [Part 1] - Functions - Test for file creation: ./lab3e.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab3e.py'), msg=error_output)

    def test_a(self):
        """[Lab 3] - [Investigation 3] - [Part 1] - Functions - Test for errors running: ./lab3e.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab3e.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    
    def test_a_function_list(self):
        """[Lab 3] - [Investigation 3] - [Part 1] - functions & lists - print first item in list"""
        try:
            import lab3e as lab3eStudent 
        except:
            self.fail('your script contains errors')
        expected_output = [100, 200, 300, 'six hundred']
        error_output = ''
        self.assertEqual(expected_output, lab3eStudent.give_list(), msg=error_output)
    
    def test_a1(self):
        """[Lab 3] - [Investigation 3] - [Part 1] - Functions - Test for correct shebang line: ./lab3X.py"""
        lab_file = open('./lab3e.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)

    def test_b_function_first(self):
        """[Lab 3] - [Investigation 3] - [Part 1] - functions & lists - print first item in list"""
        try:
            import lab3e as lab3eStudent 
        except:
            self.fail('your script contains errors')
        expected_output = '100'
        error_output = 'your function must return a string value(HINT: use the str() function)'
        self.assertEqual(expected_output, lab3eStudent.give_first_item(), msg=error_output)

    def test_c_function_first_and_last(self):
        """[Lab 3] - [Investigation 3] - [Part 1] - functions & lists - print last item in list"""
        try:
            import lab3e as lab3eStudent 
        except:
            self.fail('your script contains errors')
        expected_output = [100, 'six hundred']
        error_output = ''
        self.assertEqual(expected_output, lab3eStudent.give_first_and_last_item(), msg=error_output)
    
    def test_d_function_second_and_third(self):
        """[Lab 3] - [Investigation 3] - [Part 1] - functions & lists - print last item in list"""
        try:
            import lab3e as lab3eStudent 
        except:
            self.fail('your script contains errors')
        expected_output = [200, 300]
        error_output = ''
        self.assertEqual(expected_output, lab3eStudent.give_second_and_third_item(), msg=error_output)


class lab3f(unittest.TestCase):
    """All test cases for lab3f - for loops & arguments & if statements"""
    
    def test_0(self):
        """[Lab 3] - [Investigation 3] - [Part 3] - functions & lists & for loops - Test for file creation: ./lab3f.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab3f.py'), msg=error_output)

    def test_a(self):
        """[Lab 3] - [Investigation 3] - [Part 3] - functions & lists & for loops - Test for errors running: ./lab3f.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab3f.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 3] - [Investigation 3] - [Part 3] - functions & lists & for loops - Test for correct shebang line: ./lab3f.py"""
        lab_file = open('./lab3f.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)
    
    def test_b_function_add_item_to_list(self):
        """[Lab 3] - [Investigation 3] - [Part 3] - functions & lists & for loops - check for correct items in list"""
        try:
            import lab3f as lab3fStudent 
        except:
            self.fail('your script contains errors')
        tmp = lab3fStudent.add_item_to_list(lab3fStudent.my_list)
        expected_output = [ 1, 2, 3, 4, 5, 6 ]
        error_output = ''
        self.assertEqual(expected_output, lab3fStudent.my_list, msg=error_output)

    def test_c_function_add_item_to_list(self):
        """[Lab 3] - [Investigation 3] - [Part 3] - functions & lists & for loops - check for correct items in list"""
        try:
            import lab3f as lab3fStudent 
        except:
            self.fail('your script contains errors')
        tmp = lab3fStudent.add_item_to_list(lab3fStudent.my_list)
        tmp = lab3fStudent.add_item_to_list(lab3fStudent.my_list)
        expected_output = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
        error_output = ''
        self.assertEqual(expected_output, lab3fStudent.my_list, msg=error_output)
    
    def test_d_function_remove_items_from_list(self):
        """[Lab 3] - [Investigation 3] - [Part 3] - functions & lists & for loops - check for correct items in list"""
        try:
            import lab3f as lab3fStudent 
        except:
            self.fail('your script contains errors')
        tmp = lab3fStudent.remove_items_from_list(lab3fStudent.my_list, [1,5,6])
        expected_output = [ 2, 3, 4, 7, 8 ]
        error_output = ''
        self.assertEqual(expected_output, lab3fStudent.my_list, msg=error_output)
    
    def test_e_function_remove_items_from_list(self):
        """[Lab 3] - [Investigation 3] - [Part 3] - functions & lists & for loops - check for correct items in list"""
        try:
            import lab3f as lab3fStudent 
        except:
            self.fail('your script contains errors')
        tmp = lab3fStudent.remove_items_from_list(lab3fStudent.my_list, [8, 7])
        expected_output = [ 2, 3, 4 ]
        error_output = ''
        self.assertEqual(expected_output, lab3fStudent.my_list, msg=error_output)



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
        lab_name = 'CheckLab3.py'
        lab_num = 'lab3'
        print('Checking for updates...')
        if ChecksumLatest(url='https://raw.githubusercontent.com/Seneca-CDOT/ops435/master/LabCheckScripts/' + lab_name) != ChecksumLocal(filename='./' + lab_name):
            print()
            print(' There is a update available for ' + lab_name + ' please consider updating:')
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


        
