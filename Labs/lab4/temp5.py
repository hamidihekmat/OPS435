

course_name = 'Open System Automation'
course_code = 'OPS435'
course_number = 435

print(course_name)
print(course_code)
print(str(course_number))
print(course_name + ' ' + course_code + ' ' + str(course_number))


print(course_name.lower())         # Returns a string in lower-case letters
print(course_name.upper())         # Returns a string in upper-case letters
print(course_name.swapcase())      # Returns a string with upper-case and lower-case letters swapped
print(course_name.title())         # Returns a string with upper-case first letter of each word, lowercase for remaining text
print(course_name.capitalize())    # Returns a string with upper-case first letter only, lowercase for remaining text



lower_name = course_name.lower()    # Save returned string lower-case string inside new string variable
print(lower_name)

print('split string into spaces')
list_of_strings = lower_name.split(' ')     # Split string on spaces and store the list in a variable
print(list_of_strings)                      # Display list
print(list_of_strings[0])                   # Display first item in list
