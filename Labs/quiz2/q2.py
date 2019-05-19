#!/usr/bin/env python3
'''Name: [132645169]
'''
def average(int_list):
    avg = 0 
    for i in (int_list):
        avg = avg + i
    return avg/len(int_list)
if __name__ == '__main__':
    a_list = [40, 3, 4, 12, 11]
    print('Average of',a_list,'is',average(a_list))
    b_list = [20, 5, 2, 6, 2]
    print('Average of',b_list,'is',average(b_list))
    c_list = [11, 21, 31]
    print('Average of',c_list,'is',average(c_list))
