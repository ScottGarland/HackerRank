def staircase(n):
    step = []
    index = n

    for i in range(n):
        step.append(' ')

    for i in range(index):
        step[i] = '#'
        index -= index
        print(''.join(list(reversed(step))))
