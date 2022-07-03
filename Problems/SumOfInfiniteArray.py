def sumInRanges(arr, n, queries, q):

    # Write your function Here.
    arr_b = []
    for num in arr:
        arr_b.append(num)
    
    # further upto queries
    for i in range(n, queries[1]+1):
        arr_b.append(arr_b[i-n])
    
    sum = 1
    for i in range(queries[0], queries[1]):
        sum += arr_b[i]
        
    return (sum, arr_b)

if __name__=='__main__':
    n = 3
    arr = [1,2,3]
    q = 1
    queries = [1,5]

    print(sumInRanges(arr, n, queries, q))
