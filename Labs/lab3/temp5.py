#!/usr/bin/env python3

def describe_temperature(temp):
	if temp > 30:
		return 'hot'
	elif temp < 0:
		return 'cold'
	elif temp == 20:
		return 'perfect'
	return 'ok'


print(describe_temperature(50))
print(describe_temperature(20))
print(describe_temperature(-50))
print(describe_temperature(25))
print(describe_temperature(10))
