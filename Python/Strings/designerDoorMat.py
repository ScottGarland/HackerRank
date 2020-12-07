# https://www.hackerrank.com/challenges/designer-door-mat/problem

line = input().split()
n = int(line[0])
m = int(line[1])
p = int(n - 2) #number of pipes
q = int((m - 7) / 2) #7 is length of 'WELCOME'
d = int((m - 3) / 2) #numer of dashes

dash = '-'
pipe = '.|.'
matToMiddle = []
welcome_line = q*dash + 'WELCOME' + q*dash 

for i in range(0,(int(n/2))):
    matToMiddle.insert(0,p*pipe)
    p = p - 2

for row in matToMiddle:
    print(d*dash + row + d*dash)
    d = d - 3

print(welcome_line)

d = d + 3
revMat = matToMiddle[::-1]
for row in revMat:
    print(d*dash + row + d*dash)
    d = d + 3
