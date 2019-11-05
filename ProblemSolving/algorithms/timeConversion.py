#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hh = s[0:2]
    XM = s[-2] + s[-1]

    if XM == 'PM':
        if hh != '12':
            hh = str(int(hh) + 12)
    
    if XM == 'AM':
        if hh == '12':
            hh = '00'

    return hh + s[2:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
