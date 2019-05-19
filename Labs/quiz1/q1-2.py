#!/usr/bin/env python3

import sys

a = int(sys.argv[1])
b = sys.argv[2]
if (a) == 0:
    print('ValueError: the first argument must be greater than 0.')
    sys.exit()
else:
   print(a * b)
