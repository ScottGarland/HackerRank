# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for i in range(n):
    T = input()
    even = []
    odd = []

    for j in range(len(T)):
        if j % 2 == 0:
            even.append(T[j])
        if j % 2 != 0:
            odd.append(T[j])

    print("{} {}".format(''.join(even),''.join(odd)))
