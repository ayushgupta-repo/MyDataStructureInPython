# Defining Bubble Sort: It is the sorting algorithm in which repeatedly two adjancet pairs are compared and if they are in wrong order then they get swapped

# def bubbleSort(customList):
#     for i in range(len(customList)-1):
#         for j in range(len(customList)-i-1):
#             if customList[j] > customList[j+1]:
#                 # do swapping
#                 customList[j], customList[j+1] = customList[j+1], customList[j]
    
#     print(customList)

# To make it more optimized
def bubbleSort(customList):

    for i in range(len(customList)-1):
        swapped = False # to check if swapped is not happening then it means list is sorted
        
        # As after each sorting phase last element reaches its position so for further phases we don't need to compare other elements with it so extra -i is given in the below condition
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                # do swapping
                customList[j], customList[j+1] = customList[j+1], customList[j]
                swapped = True

        if not swapped:
            break
    
    print(customList)

cList = [6, 3, 8, 9, 1]
bubbleSort(cList)