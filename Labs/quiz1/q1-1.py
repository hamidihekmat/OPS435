#! /usr/bin/env python3

ccb_u6 = 541
ccb_6to17 = 456
child_u6 = int(input('what is the number of child under the age of 6?'))
child_6to17 = int(input('what is the number of child aged 6 to 17?'))
ccb_total = (ccb_u6 * child_u6) + (ccb_6to17 * child_6to17)
print('The total Canada Child Benefit for the family is ' + str(ccb_total))
