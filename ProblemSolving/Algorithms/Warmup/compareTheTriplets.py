# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compareTriplets(a, b):
    a_count = 0
    b_count = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            a_count = a_count + 1
        elif a[i] == b[i]:
            continue
        elif a[i] < b[i]:
            b_count = b_count + 1
    return a_count, b_count
