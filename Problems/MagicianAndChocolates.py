def maximumChocolates(arr, k):
    # Write your code here.
    count = 0
    total = 0
    
    while count != k:
        num = max(arr)
        total += num
        
        # for i in arr:
        #     if i == num:
        #         i = i//2
        #         break

        for i in range(len(arr)):
            if arr[i] == num:
                arr[i] = arr[i]//2
                break
        
        count += 1
    
    return arr, total

print(maximumChocolates([10, 4, 7, 22], 2))