# Insertion Sort: In this type of algorithm first element from the unsorted array is picked and being compared to the sorted array elements and finds the position to be stored in the sorted array.

def insertionSort(customList):
    # We start from index 1 as we consider that element at 0 is already in Sorted array so that we can do comparison
    for i in range(1, len(customList)):
        key = customList[i] # picking first element of the unsorted array
        j = i-1 # previous/sorted array element index from back starts

        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j] # j+1 means current position from where the element is picked
            j -= 1 # decrementing to do comparison with other sorted array elements

        customList[j+1] = key # after finding exact position in sorted array
    
    print(customList)

cList = [6, 3, 8, 9, 1]
insertionSort(cList)