def firstAndLastPosition(arr, n, k):

    # Write your code here
    firstOccurence = -1

    secondOccurence = -1
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == k:
            secondOccurence = i
            break
    
    for i in range(secondOccurence):
        if arr[i] == k:
            firstOccurence = i
            break
            
    return (firstOccurence, secondOccurence)
    