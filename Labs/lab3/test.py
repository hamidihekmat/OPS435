#!/usr/bin/env python3

def square(number):
	return number ** 2
print(square(5))
square(10)
square(12)
square(square(2))

def sum_numbers(number1, number2):
	return int(number1) + int(number2)
print(sum_numbers(5, 10))
print(sum_numbers(50, 100))
print(square(sum_numbers(5, 5)))
