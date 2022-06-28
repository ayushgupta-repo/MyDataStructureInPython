# Bucket Sort: Steps;
# 1. Divide elements into numberOfBuckets (calculated using formula)
# 2. Sort buckets individualy
# 3. Merge sorted buckets

import math


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        
        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        
        customList[j+1] = key
    
    return customList

def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    # setting maxValue
    maxValue = max(customList)
    # creating temp array to store buckets
    arr = []

    # creating buckets on the basis of numberOfBuckets into temp array
    for i in range(numberOfBuckets):
        arr.append([])

    # storing elements on the basis of formula into appropriate buckets
    for i in customList:
        # to store bucket number
        index_b = math.ceil(i * numberOfBuckets / maxValue)
        arr[index_b-1].append(i) # index_b-1 is done as index starts from 0

    # sorting individual buckets using any algorithm
    # NOTE: Keep in mind that the algorithm which will be used is going to decide the time complexity of Bucket Sort algorithm
    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])

    # merging sorted buckets

    k = 0

    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1

    return customList

cList = [6, 3, 8, 9, 1]
print(bucketSort(cList))