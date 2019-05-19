#!/usr/bin/env python3

a = int(input('Assign a number to (a) '))
b = int(input('Assign a number to (b) '))
if a > b:
    print('a is greater than b')
elif a < b:
    print('b is greater than a')
else:
    print('a is not greater than b')
    print('a is not less than b')
    print('Therefore, a is equal to b')
