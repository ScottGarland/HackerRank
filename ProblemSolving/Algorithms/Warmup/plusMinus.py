# https://www.hackerrank.com/challenges/plus-minus/problem

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
