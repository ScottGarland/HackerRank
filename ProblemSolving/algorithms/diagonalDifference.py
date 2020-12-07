# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    diag1 = 0
    diag2 = 0
    k = n
    for i in range(n):
        diag1 = diag1 + arr[i][i]
        diag2 = diag2 + arr[i][k-1]
        k = k - 1

    return abs(diag1 - diag2)
