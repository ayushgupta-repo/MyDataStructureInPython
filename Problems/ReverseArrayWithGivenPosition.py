
def reverseNumber(num):
    left_marker = 0
    right_marker = len(num)-1

    while left_marker <= right_marker:
        # do swapping
        num[left_marker], num[right_marker] = num[right_marker], num[left_marker]
        left_marker += 1
        right_marker -= 1

    return num

def reverseArray(arr, m):
    # Write your code here.
    finalArr = arr[:m+1]
    # reversingPart = arr[m+1:]
    
    # reversingPart.reverse()
    
    # for i in reversingPart:
    #     finalArr.append(i)
        
    # return finalArr
    reversedPart = reverseNumber(arr[m+1:])

    for i in reversedPart:
        finalArr.append(i)

    return finalArr

print(reverseArray([1,2,3,4,5,6], 3))