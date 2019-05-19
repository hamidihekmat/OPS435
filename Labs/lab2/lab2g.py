#!/usr/bin/env python3
import sys
timer = 3
if len(sys.argv) != 2:
    while timer !=0:
        print(timer)
        timer = timer - 1
    print('blast off!')
else :
    count = int(sys.argv[1])
    while count !=0:
        print(count)
        count = count - 1
    print('blast off!')
