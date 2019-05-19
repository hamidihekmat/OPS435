#! /usr/bin/env python3

t1 = ('Prime', 'Ix', 'Secundus', 'Caladan')
t2 = (1, 2, 3, 4, 5, 6)

list2 = [ 'uli101', 'ops235', 'ops335', 'ops435', 'ops535', 'ops635' ]
print(list2)
list2[0]= 'ica100'
print(list2[0])
print(list2)

print(t1[0])
print('Geidi' in t1)
t3 = t2[2:4]
print(t3)

print('testing loop code in tuples')
for item in t1:
	print('item: ' + item)
