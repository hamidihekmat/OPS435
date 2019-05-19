#!/usr/bin/env python3

def function1():
    # This variable 'a' is completely unrelated to the variable 'a' in function2():
    a = 'Andrew 1'
    print(a)

def function2():
    # This variable 'a' is completely unrelated to the variable 'a' in function1():
    a = 'Andrew 2'
    print(a)

# Note that you cannot make any of the following print() functions work because neither of 
# the variables '''a''' exist in this scope (outside the function where they were defined):
a = 'Andrew 500'
print(a)
function1()
print(a)
function2()
print(a)
function1()
function2()
