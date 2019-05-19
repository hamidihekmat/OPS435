l2 = [1, 2, 3, 4, 5]
l3 = [4, 5, 6, 7, 8]
temporary_set = set(l2).intersection(set(l3))
new_list = list(temporary_set)  # '''set()''' can make lists into sets. '''list()''' can make sets into lists.
print(new_list)
