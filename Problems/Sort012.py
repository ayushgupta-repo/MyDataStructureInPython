def sort012(arr, n) :

	# write your code here
    # don't return anything 
#     arr.sort()
    arr0 = []
    arr1 = []
    arr2 = []
    
    for i in arr:
        if i == 0:
            arr0.append(i)
        elif i == 1:
            arr1.append(i)
        else:
            arr2.append(i)

    for i in arr1:
        arr0.append(i)
    
    for j in arr2:
        arr0.append(j)

    arr = arr0

    return arr

if __name__=='__main__':
    arr = [0, 1, 2, 2, 1, 0]
    print(sort012(arr, len(arr)))