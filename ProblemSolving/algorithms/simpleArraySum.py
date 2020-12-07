# https://www.hackerrank.com/challenges/simple-array-sum/problem

def simpleArraySum(ar):
    sum = 0
    for i in range(len(ar)):
        sum = sum + ar[i]
    return sum
