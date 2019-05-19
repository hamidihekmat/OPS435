#!/usr/bin/env python3

import sys
if len(sys.argv) != 3:
	print('Usage: ' + sys.argv[0] + ' name age')
	sys.exit()
else : 
	name = sys.argv[1]
	age = sys.argv[2]
	print('Hi ' + name + ', you are ' + age + ' years old.')

