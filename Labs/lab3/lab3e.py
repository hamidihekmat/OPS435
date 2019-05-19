#!/usr/bin/env python3

# Create the list called "my_list" here, not within any function defined below.
# That makes it a global variable. We'll talk about that in another lab.
mylist = [100, 200, 300, 'six hundred']

def give_list():
	return mylist
    # Does not accept any arguments
    # Returns all of the global variable my_list unchanged

def give_first_item():
    # Does not accept any arguments
    # Returns a single string that is the first item in the global my_list
	return str(mylist[0])

def give_first_and_last_item():
	return [mylist[0], mylist[-1]] 
    # Does not accept any arguments
    # Returns a list that includes the first and last items in the global my_list

def give_second_and_third_item():
	return mylist[1:3]
    # Does not accept any arguments
    # Returns a list that includes the second and third items in the global my_list

if __name__ == '__main__':   # This section also referred to as a "main code"
	print(give_list())
	print(give_first_item())
	print(give_first_and_last_item())
	print(give_second_and_third_item())
