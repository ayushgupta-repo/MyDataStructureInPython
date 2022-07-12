
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
                    arr = arr[j:]
                    n = n - j
                    i = 0
                    j += 1
                    if j == m:
                        break
                else:
                    i += 1
            i = 0
            j += 1
    else:
        while i < n:
            while j < m and i < n:
                if arr[i] == brr[j]:
                    common.append(arr[i])
                    arr = arr[i:]
                    n = n - i
                    j = 0
                    i += 1
                    if i == n:
                        break
                else:
                    j += 1
            j = 0
            i += 1
    
    return common
                
# print(findArrayIntersection([1, 2, 2, 2, 3, 4], 6, [2, 2, 3, 3], 4))
# print(findArrayIntersection([1, 2, 3], 3, [3, 4], 2))
print(findArrayIntersection([0, 0, 5, 5, 8, 10, 10, 11, 12, 15, 17, 17, 17], 13, [1, 2, 4, 5, 5, 6, 9, 9, 12, 12, 12], 11))