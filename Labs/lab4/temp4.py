dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Postal Code': 'M3J3M6'}
print(dict_york.values())
a = dict_york.keys()
print(a)
print('printing individual values')
print(dict_york['Address'])
print(dict_york['Postal Code'])
# adding new values
dict_york['Country'] = 'Canada'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())
dict_york['Province'] = 'BC'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())
#changing values in dictionaries
dict_york['Province'] = 'ON'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

#converting dictonary keys to list
list_of_keys = list(dict_york.keys())
print(list_of_keys[0])

#used in loops

list_of_keys = list(dict_york.keys())
for key in list_of_keys:
    print(key)
for value in dict_york.values():
    print(value)
