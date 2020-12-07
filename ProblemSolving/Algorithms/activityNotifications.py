# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

def activityNotificationsTimeout(expenditure, d):
    """
    This function is the first attempt which should work, but it times out.
    
    :param: expenditure
    :param: d
    :returns: integer value for the number of notifications to be sent warning the client
    :rtyp: int    
    """
    arr = expenditure[:]
    noti_total = 0 # count for the total number of notifications
    size = len(expenditure) # size of the expenditure array
    
    # we want to loop through the expenditures starting at the index designated by
    # d, the number of trailing days. This is because the trailing days starts from 
    # index 0 to d. We want to iterate through all expenditures. Time complexity is
    # O(n(nlogn)) due to looping with a sort inside.
    for index in range(d, size):
        # this is the sorted range of expenditures needed to find the median
        median_range = sorted(arr[ (index - d) : index ]) # time complexity of O(nlogn)
        
        # if d is even, then we take the average of the middle two numbers
        # we need to do the integer division so we get the floor value
        # when it cocatenates. This is because we can't have a non-integer index.
        if d % 2 == 0:
            median_numerator = median_range[(d//2) - 1] + median_range[((d + 1)//2)]
            median = median_numerator / 2
        
        # else it's odd, and the median is the middle number
        else:
            median = median_range[((d + 1)//2) - 1]
            
        # now that the median is calculated, we can add to the noti_total
        if arr[index] >= (2 * median):
                noti_total = noti_total + 1
    
    return noti_total

def calculate_median(noti_freq, is_even, d):
    """
    This function is so I can calculate the medians needed with the trailing numbers. If I have the code inside
    the main activityNotifications() function, the wrong median values get calculate. This also helps with
    compartmentalization.

    :param: noti_freq
    :param: is_even
    :param: d
    :returns: median
    """

    sum_temp = 0 # temp variable to store some sums
    position = None # position of the median value we want
    
    # These if statements are outlined in the problem to determin the median of an odd or even amount
    # of trailing days
    if is_even == True: # d % 2 == 0
        for index, value in enumerate(noti_freq):
            sum_temp = sum_temp + value
            
            if sum_temp > (d // 2):
                return index
            
            if sum_temp == (d // 2):
                position = index
                return (position + (position + 1)) / 2

    else: # d is odd: d % 2 != 0
        for index, value in enumerate(noti_freq):
            sum_temp = sum_temp + value

            if sum_temp > (d // 2):
                return index
            

def activityNotifications(expenditure, d):
    """
    Function to determine the number of fraudulent notifications to be sent.

    To deal with the runtime errors I get in previous attempts, this one will take advatage
    of the constraints on d and expenditures since they are close enough in value in order to
    do a counting-sort.
    1 <= d <= n
    0 <= expenditures[i] <= 200

    The time complexity of this function is O(n log n)

    :param: expenditure array
    :param: d number of trailing days
    :returns: integer value for the number of notifications to be sent warning the client
    :rtyp: int    
    """
    
    size = len(expenditure) # size of the expenditure array
    max_expend = 200 # the max expentiture value constraint
    noti_total = 0
    noti_freq = []
    is_even = False # to determine if d is even, initialize as False

    if d % 2 == 0:
        is_even = True

    # we can build a frequency table of sorts in order to count the number of times an expenditure
    # value shows up in the d previous trailing days. This count will start at 0.

    # initializing the frequency array
    for i in range(max_expend + 1):
        noti_freq.append(0)

    for i in range(d):
        noti_freq[expenditure[i]] = noti_freq[expenditure[i]] + 1

    # now we can iterate through the indeces started at d
    day0 = 0
    for i in range(d, size):
    
        median = calculate_median(noti_freq, is_even, d)

        if expenditure[i] >= (2*median):
            # increase the noti_total if this condition is met
            noti_total = noti_total + 1

        noti_freq[expenditure[day0]] = noti_freq[expenditure[day0]] - 1 # decrease the freq
        noti_freq[expenditure[i]] = noti_freq[expenditure[i]] + 1 # increase the freq
        
        day0 = day0 + 1 # this moves the trailing days up the array

    return noti_total
