#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    tally = {'pos' : 0, 'neg' : 0, 'zero' : 0}

    for element in arr:
        if element > 0:
            tally['pos'] += 1
        elif element < 0:
            tally['neg'] += 1
        elif element == 0:
            tally['zero'] += 1
    
    print(f"{tally['pos']/n : .6f}")
    print(f"{tally['neg']/n : .6f}")
    print(f"{tally['zero']/n : .6f}")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
