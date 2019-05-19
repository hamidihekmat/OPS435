list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]

# Squares each item in a list of numbers, returns new list with squared numbers
def square_list(number_list):
    new_list = []
    for number in number_list:
        new_list.append(number * number)
    return new_list

new_list_of_numbers = square_list(list_of_numbers)
print(list_of_numbers)
print(new_list_of_numbers)
