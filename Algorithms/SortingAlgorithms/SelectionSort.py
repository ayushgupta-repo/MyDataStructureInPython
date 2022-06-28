# Selection Sort: In this sorting algorithm we first find the minimum element from the unsorted array and swap it with first element and then move/shift it to the sorted array and this will not be considered in further sorting operation phase.

# def selectionSort(customlist):
#     # This time last element is also included
#     for i in range(len(customlist)):
#         min_index = i

#         # also after comparison and swapping we don't need leftmost elements as they are in sorted array part so we doing i+1
#         # now comparing the picked minimum element with its successive elements and as per the comparison min_index may be changed or not
#         for j in range(i+1, len(customlist)):
#             if customlist[min_index] > customlist[j]:
#                 min_index = j # updating min_index
            
#         # now swapping min_index with i
#         customlist[i], customlist[min_index] = customlist[min_index], customlist[i]
    
#     print(customlist)

def selectionSort(customlist):
    # This time last element is also included
    for i in range(len(customlist)):
        min_index = i

        # also after comparison and swapping we don't need leftmost elements as they are in sorted array part so we doing i+1
        # now comparing the picked minimum element with its successive elements and as per the comparison min_index may be changed or not
        for j in range(i+1, len(customlist)):
            if customlist[min_index] > customlist[j]:
                min_index = j # updating min_index
        
        # for optimizatin of algorithm we are addding flow control as below
        if i != min_index:
            # now swapping min_index with i
            customlist[i], customlist[min_index] = customlist[min_index], customlist[i]
    
    print(customlist)

cList = [6, 3, 8, 9, 1, 7]
selectionSort(cList)
