
def miniMaxSum(arr):
    sort = sorted(arr)
    large = sort.pop(len(arr)-1)
    small = sort.pop(0)
    max_sum = large
    min_sum = small

    for i in sort:
        max_sum += i
        min_sum += i
    
    print(min_sum, max_sum)
