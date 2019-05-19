#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
	dictinary = dict(zip(keys, values))
	return dictinary
def shared_values(dict1, dict2):    # Place code here - refer to function specifics in section below
	list1 = []
	list2 = []
	for index in dict1.values():
		list1.append(index)
	for index in dict2.values():
		list2.append(index)
	
	list3 = set(list1).intersection(set(list2))
	return list3
if __name__ == '__main__':
	york = create_dictionary(list_keys, list_values)
	print('York: ', york)
	common = shared_values(dict_york, dict_newnham)
	print('Shared Values', common)
