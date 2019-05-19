#!/usr/bin/env python3
import sys

def quiz3(input):
	if len(input) == 6:
		a = ('Sorry, ' + str(input)+ ' has only 6 letters.')
		print('Please give me a nine-letter word.')
		return a
	elif len(input) == 1:
		a = ('Sorry ' + str(input) + ' has only 1 letter.')
		print('Please give me a nine letter word.')
		return a
	elif len(input) == 9:
		print('Thank you for your cooperation.')
		print('Here is the enter code: ' + str(input[::2]))
		a = str(input[::2])
		b = ('And here the exit code is: ' +  a[::-1])
		return b
	else:
		print('Sorry, ' +str(input) + ' has ' + str(len(input)) + ' lines')
		return ('Please give me a nine letter word.')	
print(quiz3(sys.argv[1]))
