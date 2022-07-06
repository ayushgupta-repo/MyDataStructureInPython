
def findArrayIntersection(arr, n, brr, m):
    # Write your code here
    # Return a list containing all the common elements in arr and brr.
    
    common = []
    i = 0
    j = 0
    
    if n > m:
        while j < m:
            while i < n:
                if brr[j] == arr[i]:
                    common.append(brr[j])
                    i += 1
                    j += 1
                else:
                    i += 1
            i = 0
            j += 1
    else:
        while i < n:
            while j < m and i < n:
                if arr[i] == brr[j]:
                    common.append(arr[i])
                    i += 1
                    j += 1
                else:
                    j += 1
            j = 0
            i += 1
    
    return common
                
# print(findArrayIntersection([1, 2, 2, 2, 3, 4], 6, [2, 2, 3, 3], 4))
# print(findArrayIntersection([1, 2, 3], 3, [3, 4], 2))
print(findArrayIntersection([7, 9, 9], 3, [6, 7, 7, 7, 9, 9, 9], 7))