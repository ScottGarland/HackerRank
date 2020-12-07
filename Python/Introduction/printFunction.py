# https://www.hackerrank.com/challenges/python-print/problem

nums = []
final = ''

for i in range(1,n+1):
    nums.append(i)

print(*nums, sep='')
