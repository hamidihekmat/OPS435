#!/usr/bin/env python3

courses = [ 'uli101', 'ops235', 'ops335', 'ops435', 'ops535', 'ops635' ]
print(courses[0])
courses[0] = 'eac150'
print(courses[0])
print(courses)

courses.append('ops235')    # Add a new item to the end of the list
print(courses)

courses.insert(0, 'hwd101') # Add a new item to the specified index location
print(courses)

courses.remove('ops335')    # Remove first occurrence of value
print(courses)

sorted_courses = courses.copy() # Create a copy of the courses list
sorted_courses.sort()           # Sort the new list
print(courses)
print(sorted_courses)
