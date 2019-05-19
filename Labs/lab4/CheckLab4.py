#!/usr/bin/env python3

import subprocess
import unittest
import sys
import os
import hashlib
import urllib.request

class lab4a(unittest.TestCase):
    """All test cases for lab4a - sets"""
    
    def test_0(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Data Structures - Test for file creation: ./lab4a.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab4a.py'), msg=error_output)

    def test_a(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Data Structures - Test for errors running: ./lab4a.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab4a.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Data Structures - Test for correct shebang line: ./lab4a.py"""
        lab_file = open('./lab4a.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)


    def test_a_function_join(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function join_sets() fails without 2 arguments"""
        with self.assertRaises(Exception) as context:
            import lab4a as lab4aStudent
            lab4aStudent.join_sets()
    
    def test_b_function_join(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function match_sets() fails without 2 arguments"""
        with self.assertRaises(Exception) as context:
            import lab4a as lab4aStudent
            lab4aStudent.match_sets()
    
    def test_c_function_join(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function diff_sets() fails without 2 arguments"""
        with self.assertRaises(Exception) as context:
            import lab4a as lab4aStudent
            lab4aStudent.diff_sets()

    def test_d_function_join_sets(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function join_sets() joins sets together {1,2,3,4,5} and {2,1,0,-1,-2} """
        # Try to import before testing
        try:
            import lab4a as lab4aStudent
        except:
            self.fail('lab4a.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem joining(HINT: join_sets({1,2,3,4,5}, {2,1,0,-1,-2}))'
        set1 = {1,2,3,4,5}
        set2 = {2,1,0,-1,-2}
        self.assertTrue(lab4aStudent.join_sets(set1,set2) == set1|set2, msg=error_output)
    
    def test_e_function_join_sets(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function join_sets() joins sets together"""
        # Try to import before testing
        try:
            import lab4a as lab4aStudent
        except:
            self.fail('lab4a.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem joining(HINT: try joining different sets together))'
        set1 = set(range(5,9))
        set2 = set(range(1,5))
        self.assertTrue(lab4aStudent.join_sets(set1,set2) == set1|set2, msg=error_output)

    def test_f_function_match_sets(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function match_sets()"""
        # Try to import before testing
        try:
            import lab4a as lab4aStudent
        except:
            self.fail('lab4a.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with intersection(HINT: try matching different sets together))'
        set1 = set(range(1,10))
        set2 = set(range(5,15))
        self.assertTrue(lab4aStudent.match_sets(set1,set2) == set1&set2, msg=error_output)

    def test_g_function_match_sets(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function match_sets()"""
        # Try to import before testing
        try:
            import lab4a as lab4aStudent
        except:
            self.fail('lab4a.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with intersection(HINT: try matching different sets together))'
        set1 = set(range(5,9))
        set2 = set(range(1,5))
        self.assertTrue(lab4aStudent.match_sets(set1,set2) == set1&set2, msg=error_output)
    
    def test_h_function_diff_sets(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function diff_sets()"""
        # Try to import before testing
        try:
            import lab4a as lab4aStudent
        except:
            self.fail('lab4a.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with intersection(HINT: try matching different sets together))'
        set1 = set(range(1,10))
        set2 = set(range(5,15))
        self.assertTrue(lab4aStudent.diff_sets(set1,set2) == set1^set2, msg=error_output)

    def test_i_function_diff_sets(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function diff_sets()"""
        # Try to import before testing
        try:
            import lab4a as lab4aStudent
        except:
            self.fail('lab4a.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with intersection(HINT: try matching different sets together))'
        set1 = {1,2,3,4,5}
        set2 = {2,1,0,-1,-2}
        self.assertTrue(lab4aStudent.diff_sets(set1,set2) == set1^set2, msg=error_output)


class lab4b(unittest.TestCase):
    """All test cases for lab4b - sets"""

    def test_0(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Data Structures - Test for file creation: ./lab4b.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab4b.py'), msg=error_output)

    def test_a(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Data Structures - Test for errors running: ./lab4b.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab4b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Data Structures - Test for correct shebang line: ./lab4b.py"""
        lab_file = open('./lab4b.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)


    def test_a_function_join(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function join_lists() fails without 2 arguments"""
        with self.assertRaises(Exception) as context:
            import lab4b as lab4bStudent
            lab4bStudent.join_lists()

    def test_b_function_join(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function match_lists() fails without 2 arguments"""
        with self.assertRaises(Exception) as context:
            import lab4b as lab4bStudent
            lab4bStudent.match_lists()

    def test_c_function_join(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function diff_lists() fails without 2 arguments"""
        with self.assertRaises(Exception) as context:
            import lab4b as lab4bStudent
            lab4bStudent.diff_lists()

    def test_d_function_join_lists(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function join_lists() joins lists together {1,2,3,4,5} and {2,1,0,-1,-2} """
        # Try to import before testing
        try:
            import lab4b as lab4bStudent
        except:
            self.fail('lab4b.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem joining(HINT: join_lists({1,2,3,4,5}, {2,1,0,-1,-2}))'
        list1 = [1,2,3,4,5]
        list2 = [2,1,0,-1,-2]
        self.assertTrue(lab4bStudent.join_lists(list1,list2) == list(set(list1)|set(list2)), msg=error_output)

    def test_e_function_join_lists(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function join_lists() joins lists together"""
        # Try to import before testing
        try:
            import lab4b as lab4bStudent
        except:
            self.fail('lab4b.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem joining(HINT: try joining different lists together))'
        list1 = list(range(5,9))
        list2 = list(range(1,5))
        self.assertTrue(lab4bStudent.join_lists(list1,list2) == list(set(list1)|set(list2)), msg=error_output)

    def test_f_function_match_lists(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function match_lists()"""
        # Try to import before testing
        try:
            import lab4b as lab4bStudent
        except:
            self.fail('lab4b.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with intersection(HINT: try matching different lists together))'
        list1 = list(range(1,10))
        list2 = list(range(5,15))
        self.assertTrue(lab4bStudent.match_lists(list1,list2) == list(set(list1)&set(list2)), msg=error_output)

    def test_g_function_match_lists(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function match_lists()"""
        # Try to import before testing
        try:
            import lab4b as lab4bStudent
        except:
            self.fail('lab4b.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with intersection(HINT: try matching different lists together))'
        list1 = list(range(5,9))
        list2 = list(range(1,5))
        self.assertTrue(lab4bStudent.match_lists(list1,list2) == list(set(list1)&set(list2)), msg=error_output)

    def test_h_function_diff_lists(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function diff_lists()"""
        # Try to import before testing
        try:
            import lab4b as lab4bStudent
        except:
            self.fail('lab4b.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with intersection(HINT: try matching different lists together))'
        list1 = list(range(1,10))
        list2 = list(range(5,15))
        self.assertTrue(lab4bStudent.diff_lists(list1,list2) == list(set(list1)^set(list2)), msg=error_output)

    def test_i_function_diff_lists(self):
        """[Lab 4] - [Investigation 1] - [Part 2] - Sets - function diff_lists()"""
        # Try to import before testing
        try:
            import lab4b as lab4bStudent
        except:
            self.fail('lab4b.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with intersection(HINT: try matching different lists together))'
        list1 = [1,2,3,4,5]
        list2 = [2,1,0,-1,-2]
        self.assertTrue(lab4bStudent.diff_lists(list1,list2) == list(set(list1)^set(list2)), msg=error_output)


class lab4c(unittest.TestCase):
    """All test cases for lab4c - dictionaries"""

    def test_0(self):
        """[Lab 4] - [Investigation 1] - [Part 3] - Data Structures - Test for file creation: ./lab4c.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab4c.py'), msg=error_output)

    def test_a(self):
        """[Lab 4] - [Investigation 1] - [Part 3] - Data Structures - Test for errors running: ./lab4c.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab4c.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: make sure you copied the script exactly!)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 4] - [Investigation 1] - [Part 3] - Data Structures - Test for correct shebang line: ./lab4c.py"""
        lab_file = open('./lab4c.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)


    def test_b_function_create_dictionary(self):
        """[Lab 4] - [Investigation 1] - [Part 3] - Data Structures - function create_dictionary() fails without 2 arguments"""
        with self.assertRaises(Exception) as context:
            import lab4c as lab4cStudent
            lab4cStudent.create_dictionary()
    
    #~ def test_c_function_split_dictionary(self):
        #~ """[Lab 4] - [Investigation 1] - [Part 3] - Data Structures - function split_dictionary() fails without 1 argument1"""
        #~ with self.assertRaises(Exception) as context:
            #~ import lab4c as lab4cStudent
            #~ lab4cStudent.split_dictionary()

    def test_d_function_shared_values(self):
        """[Lab 4] - [Investigation 1] - [Part 3] - Data Structures - function shared_values() fails without 2 arguments"""
        with self.assertRaises(Exception) as context:
            import lab4c as lab4cStudent
            lab4cStudent.shared_values()

    def test_e_function_create_dictionary(self):
        """[Lab 4] - [Investigation 1] - [Part 3] - Data Structures - function create_dictionary()"""
        # Try to import before testing
        try:
            import lab4c as lab4cStudent
        except:
            self.fail('lab4c.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with function(HINT:))'
        dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
        list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
        list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']
        self.assertTrue(lab4cStudent.create_dictionary(list_keys,list_values) == dict_york, msg=error_output)
    
    def test_f_function_create_dictionary(self):
        """[Lab 4] - [Investigation 1] - [Part 3] - Data Structures - function create_dictionary()"""
        # Try to import before testing
        try:
            import lab4c as lab4cStudent
        except:
            self.fail('lab4c.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with function(HINT:))'
        dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'United States', 'Postal Code': 'M3J3M6', 'Province': 'BC'}
        list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
        list_values = ['70 The Pond Rd', 'Toronto', 'United States', 'M3J3M6', 'BC']
        self.assertTrue(lab4cStudent.create_dictionary(list_keys,list_values) == dict_york, msg=error_output)

    #~ def test_g_function_split_dictionary(self):
        #~ """[Lab 4] - [Investigation 1] - [Part 3] - Data Structures - function split_dictionary()"""
        #~ # Try to import before testing
        #~ try:
            #~ import lab4c as lab4cStudent
        #~ except:
            #~ self.fail('lab4c.py contains errors(HINT: run the function and fix errors')
        #~ error_output = 'problem with function(HINT:))'
        #~ dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'United States', 'Postal Code': 'M3J3M6', 'Province': 'BC'}
        #~ list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
        #~ list_values = ['70 The Pond Rd', 'Toronto', 'United States', 'M3J3M6', 'BC']
        #~ keys, values = lab4cStudent.split_dictionary(dict_york)
        #~ self.assertTrue(set(keys) == set(list_keys), msg=error_output)
    
    #~ def test_h_function_split_dictionary(self):
        #~ """[Lab 4] - [Investigation 1] - [Part 3] - Data Structures - function split_dictionary()"""
        #~ # Try to import before testing
        #~ try:
            #~ import lab4c as lab4cStudent
        #~ except:
            #~ self.fail('lab4c.py contains errors(HINT: run the function and fix errors')
        #~ error_output = 'problem with function(HINT:))'
        #~ dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'United States', 'Postal Code': 'M3J3M6', 'Province': 'BC'}
        #~ list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
        #~ list_values = ['70 The Pond Rd', 'Toronto', 'United States', 'M3J3M6', 'BC']
        #~ keys, values = lab4cStudent.split_dictionary(dict_york)
        #~ self.assertTrue(set(values) == set(list_values), msg=error_output)
    
    def test_i_function_split_dictionary(self):
        """[Lab 4] - [Investigation 1] - [Part 3] - Data Structures - function shared_values()"""
        # Try to import before testing
        try:
            import lab4c as lab4cStudent
        except:
            self.fail('lab4c.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with function(HINT:))'
        dict1 = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'United States', 'Postal Code': 'M3J3M6', 'Province': 'BC'}
        dict2 = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
        self.assertTrue(lab4cStudent.shared_values(dict1, dict2) == set(dict1.values())&set(dict2.values()), msg=error_output)
    
    def test_j_function_split_dictionary(self):
        """[Lab 4] - [Investigation 1] - [Part 3] - Data Structures - function shared_values()"""
        # Try to import before testing
        try:
            import lab4c as lab4cStudent
        except:
            self.fail('lab4c.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with function(HINT:))'
        dict1 = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
        dict2 = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
        self.assertTrue(lab4cStudent.shared_values(dict1, dict2) == set(dict1.values())&set(dict2.values()), msg=error_output)


class lab4d(unittest.TestCase):
    """All test cases for lab4d - strings"""

    def test_0(self):
        """[Lab 4] - [Investigation 2] - [Part 1] - Strings - Test for file creation: ./lab4d.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab4d.py'), msg=error_output)

    def test_a(self):
        """[Lab 4] - [Investigation 2] - [Part 1] - Strings - Test for errors running: ./lab4d.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab4d.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: )'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 4] - [Investigation 2] - [Part 1] - Strings - Test for correct shebang line: ./lab4d.py"""
        lab_file = open('./lab4d.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line.strip(), '#!/usr/bin/env python3', msg=error_output)
    
    def test_b_function_first_five(self):
        """[Lab 4] - [Investigation 2] - [Part 1] - Strings - function first_five()"""
        # Try to import before testing
        try:
            import lab4d as lab4dStudent
        except:
            self.fail('lab4d.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with function(HINT:))'
        str1 = 'Hello World!!'
        str2 = 'Seneca College'
        num1 = 1500
        num2 = 1.50
        expected_output = 'Hello'
        output = lab4dStudent.first_five(str1)
        self.assertEqual(expected_output, output, msg=error_output)

    def test_c_function_first_five(self):
        """[Lab 4] - [Investigation 2] - [Part 1] - Strings - function first_five()"""
        # Try to import before testing
        try:
            import lab4d as lab4dStudent
        except:
            self.fail('lab4d.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with function(HINT:))'
        str2 = 'Seneca College'
        expected_output = 'Senec'
        output = lab4dStudent.first_five(str2)
        self.assertEqual(expected_output, output, msg=error_output)
    
    def test_d_function_last_seven(self):
        """[Lab 4] - [Investigation 2] - [Part 1] - Strings - function last_seven()"""
        # Try to import before testing
        try:
            import lab4d as lab4dStudent
        except:
            self.fail('lab4d.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with function(HINT:))'
        str1 = 'Hello World!!'
        str2 = 'Seneca College'
        num1 = 1500
        num2 = 1.50
        expected_output = 'World!!'
        output = lab4dStudent.last_seven(str1)
        self.assertEqual(expected_output, output, msg=error_output)

    def test_e_function_last_seven(self):
        """[Lab 4] - [Investigation 2] - [Part 1] - Strings - function last_seven()"""
        # Try to import before testing
        try:
            import lab4d as lab4dStudent
        except:
            self.fail('lab4d.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with function(HINT:))'
        str1 = 'Hello World!!'
        str2 = 'Seneca College'
        num1 = 1500
        num2 = 1.50
        expected_output = 'College'
        output = lab4dStudent.last_seven(str2)
        self.assertEqual(expected_output, output, msg=error_output)

    def test_f_function_middle_number(self):
        """[Lab 4] - [Investigation 2] - [Part 1] - Strings - function middle_number()"""
        # Try to import before testing
        try:
            import lab4d as lab4dStudent
        except:
            self.fail('lab4d.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with function(HINT:))'
        str1 = 'Hello World!!'
        str2 = 'Seneca College'
        num1 = 1500
        num2 = 1.50
        expected_output = '50'
        output = lab4dStudent.middle_number(num1)
        self.assertEqual(expected_output, output, msg=error_output)

    def test_g_function_middle_number(self):
        """[Lab 4] - [Investigation 2] - [Part 1] - Strings - function middle_number()"""
        # Try to import before testing
        try:
            import lab4d as lab4dStudent
        except:
            self.fail('lab4d.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with function(HINT:))'
        str1 = 'Hello World!!'
        str2 = 'Seneca College'
        num1 = 1500
        num2 = 1.50
        expected_output = '.5'
        output = lab4dStudent.middle_number(num2)
        self.assertEqual(expected_output, output, msg=error_output)

    def test_h_function_first_three_last_three(self):
        """[Lab 4] - [Investigation 2] - [Part 1] - Strings - function first_three_last_three()"""
        # Try to import before testing
        try:
            import lab4d as lab4dStudent
        except:
            self.fail('lab4d.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with function(HINT:))'
        str1 = 'Hello World!!'
        str2 = 'Seneca College'
        num1 = 1500
        num2 = 1.50
        expected_output = 'Helege'
        output = lab4dStudent.first_three_last_three(str1, str2)
        self.assertEqual(expected_output, output, msg=error_output)
    
    def test_i_function_first_three_last_three(self):
        """[Lab 4] - [Investigation 2] - [Part 1] - Strings - function first_three_last_three()"""
        # Try to import before testing
        try:
            import lab4d as lab4dStudent
        except:
            self.fail('lab4d.py contains errors(HINT: run the function and fix errors')
        error_output = 'problem with function(HINT:))'
        str1 = 'Hello World!!'
        str2 = 'Seneca College'
        num1 = 1500
        num2 = 1.50
        expected_output = 'Send!!'
        output = lab4dStudent.first_three_last_three(str2, str1)
        self.assertEqual(expected_output, output, msg=error_output)


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
        lab_name = 'CheckLab4.py'
        lab_num = 'lab4'
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


