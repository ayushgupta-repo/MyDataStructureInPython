# Quick Sort: Steps
# 1. Pivot is set and elements in list are divided such that left side of pivot all elements will be smaller than pivot and right side of all elements are larger than pivot.
# 2. Repeat this step until one element is present or elements get sorted

# helper method
def partition(customList, low, high):
    i = low-1 # left marker
    pivot = customList[high]

    # traversing all elements in list and do swapping operation
    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1 # left marker shifts to right
            # do swapping
            customList[i], customList[j] = customList[j], customList[i]

    # else swap pivot with greater element
    customList[i+1], customList[high] = customList[high], customList[i+1]

    return (i+1)

# main method
def quickSort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)
        quickSort(customList, low, pi-1)
        quickSort(customList, pi+1, high)

cList = [3,5,8,1,2,9,4,7,6]
quickSort(cList, 0, len(cList)-1)
print(cList)

