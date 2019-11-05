#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sort = sorted(arr)
    large = sort.pop(len(arr)-1)
    small = sort.pop(0)
    max_sum = large
    min_sum = small

    for i in sort:
        max_sum += i
        min_sum += i
    
    print(min_sum, max_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
