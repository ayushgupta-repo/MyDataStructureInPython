def findDuplicate(arr):
    # Write your code here

    left_marker = 0
    right_marker = len(arr)-1
    temp = right_marker
    
    while left_marker <= right_marker:
        if arr[left_marker] == arr[right_marker]:
            return arr[left_marker]
        else:
            if right_marker > left_marker+1:
                right_marker -= 1
            else:
                left_marker += 1
                right_marker = temp

if __name__=='__main__':
    print(findDuplicate([5, 1, 2, 3, 4, 2]))