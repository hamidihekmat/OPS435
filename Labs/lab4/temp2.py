s1 = {'Prime', 'Ix', 'Secundus', 'Caladan'}
s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}
t1 = ['po', 'pop']
print('Ix' in s1)
print('Geidi' in s1)
print('pop' in t1)
print(s2 | s3) # combines set s2 and s2 and print out the sets removing duplicates
print(s2.union(s3)) # same as ^
print(s2 & s3) # only prints the shared values
print(s2.intersection(s3)) # same as above ^


print('difference')
print(s2)
print(s3)
print(s2 - s3)
print(s2.difference(s3))

print('symmetric difference')
print(s2 ^ s3)
print(s2.symmetric_difference(s3))
