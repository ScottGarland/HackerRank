#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    step = []
    index = n

    for i in range(n):
        step.append(' ')

    for i in range(index):
        step[i] = '#'
        index -= index
        print(''.join(list(reversed(step))))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
