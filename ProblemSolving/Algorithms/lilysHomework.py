def swap_count(arr, ascend = True, descend = False):
    """
    The function counts the minimum number of swaps needed.

    :param: arr is the input array given by HackerRank
    :param: ascend is a boolean value for sorting in ascending order
    :param: descend is a boolean value for sorting in descending order
    :returns: min_count minimum number of swaps
    :rtype: int
    """
    
    arr = arr[:] # this array is copied so modifications can be done. Without this, it doesn't work
    ascend = ascend # boolean value to determine to do the algo in ascending sort order
    descend = descend # same as above but descending sort order
    reverse = None # direction for sorted() function
    error = None

    # we want to keep track of the values corresponding to a particular index, so we can 
    # use a dictionary for the purpose
    array_dictionary = {}
    for index, value in enumerate(arr): # O(n)
        array_dictionary[value] = index # value is the key, and index is the value

    if ascend == True and descend == False:
        reverse = False
    elif descend == True and ascend == False:
        reverse = True
    else:
        error = -1
        return error # both can't be true and both can't be false

    # the sorted() function in Python is a variation of a merge sort called Timsort
    # the time complexity of sorted() is O(n log n)
    sorted_array = sorted(arr, reverse = reverse)

    # we now was to loop through the input array and compare it to the sorted array
    # to count the number of swaps that need to be done in order to calculate the minimum
    # This loop has a time complexity of O(n)
    min_count = 0
    for sorted_index, value in enumerate(arr):
        sorted_value = sorted_array[sorted_index]
        input_index = array_dictionary[sorted_value] # this finds the original index assiciated with the value
    
        # now that we have the indeces, we want to check if they are in the right place.
        # They are in the right place if they are equal.
        if input_index != sorted_index:
            # make the swap if they aren't equal
            arr[input_index], arr[sorted_index] = arr[sorted_index], arr[input_index]
            min_count = min_count + 1 # increase the count for each swap
            array_dictionary[value] = input_index

    return min_count

def lilysHomework(arr):
    """
    This function returns the minimum number of swaps between elements necessary to
    sort a given array in ascending or descending order. This is because the problem
    says an array is beatiful if sorted. The given array has n distinct integers, so 
    there are no repeated values.
    
    The time complexity of this function is O(n log n).
    
    :params: arr an array of n distinct integers
    :returns: min_count the minimum number of swaps needed to sort the array
    "rtype: int
    """
    ascend_count = swap_count(arr, ascend = True, descend = False)
    descend_count = swap_count(arr, ascend = False, descend = True)
    
    if ascend_count <= descend_count:
        return ascend_count
    else:
        return descend_count
