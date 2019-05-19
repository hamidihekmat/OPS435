def h2i(obj):
    source = str(obj).lower()
    temp = '0'
    target = '0123456789abcdef'
    for c in source:
        if c in target:
            temp = temp + c
    result = int(temp,16)
    return result
a = ['10','The Pond Road','Toronto']
print(h2i(a)

# object type = string
# c = abcd
# the purpose of for loop is to loop through the sourse 
# return = 15
# return = error
