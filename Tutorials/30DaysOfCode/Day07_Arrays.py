#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    rev = arr[::-1]
    result = ''

    while len(rev):
        result += str(rev.pop(0)) + ' '

    print(result)
