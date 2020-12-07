# https://www.hackerrank.com/challenges/apple-and-orange/problem

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0 # number of hits
    orange_count = 0 # number of hits

    for i in range(len(apples)):

        if ( (apples[i] + a) >= s ) and ( (apples[i] + a) <= t ):
            apple_count += 1
    
    for i in range(len(oranges)):
        if ( (oranges[i] + b) >= s ) and ( (oranges[i] + b) <= t ):
            orange_count += 1
    
    print(apple_count)
    print(orange_count)
