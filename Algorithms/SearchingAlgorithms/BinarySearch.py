# Binary Search: Steps;
# 1. Find the middle element of the sorted array and check that this is the searchingElement or it's left or right side it might be present.
# 2. Then on the basis of comparison select the side and perform same operation
# 3. Stop when you find the searchingElement or you remained with single element and not yet able to find the searchingElement means element not present in the list.

import math

def binarySearch(array, value):
    start = 0
    end = len(array)-1

    middle = math.floor((start+end)/2)

    while not(array[middle] == value) and start <= end:
        if value < array[middle]:
            # update end
            end = middle-1
        else:
            # update start
            start = middle+1
        
        middle = math.floor((start+end)/2)

    # if found
    if array[middle] == value:
        return middle
    #otherwise
    else:
        return -1


print

print(binarySearch([1, 3, 5, 9], 5)) # returns 2

print(binarySearch([1, 3, 5, 9], 9)) # returns 3

print(binarySearch([1, 3, 5, 9], 10)) # returns -1