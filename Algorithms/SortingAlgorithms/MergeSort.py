# Merge Sort: Steps;
# 1. Divide the input array into two halves and we keep dividing them recursively until they might not be broken further
# 2. And then compare the individuals and merge them in the sorted basis

# helper method
def merge(customList, l, m, r):
    # getting left and right list length
    n1 = m-l+1
    n2 = r-m

    # craeting left and right list based on length obtained above
    L = [0]*n1
    R = [0]*n2

    # inserting elements from customList to different sides of lists
    for i in range(n1):
        L[i] = customList[l+i]
    
    for j in range(n2):
        R[j] = customList[m+1+j]

    # initalizing vars to use for merging
    i = 0
    j = 0
    k = l # initially it will be zero

    while i<n1 and j<n2:
        if L[i] < R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    
    while i<n1:
        customList[k] = L[i]
        i += 1
        k += 1
    
    while j<n2:
        customList[k] = R[j]
        j += 1
        k += 1

# main method
def mergeSort(customList, l, r):
    if l < r:
        m = (l+(r-1))//2 # getting floor value or integer value
        # calling mergeSort recursively
        mergeSort(customList, l, m) # for left side
        mergeSort(customList, m+1, r) # for right side

        # merging left and right lists
        merge(customList, l, m, r)

    return customList


cList = [6, 3, 8, 9, 1]
print(mergeSort(cList, 0, len(cList)-1))


    
