
def solution(arr, m):
    arr.sort()

    # Setting minimum difference to the largest value of the chocolate
    min_diff = arr[-1]
    for i in range(len(arr)-m+1):
        j = i+m-1

        if arr[j]-arr[i] < min_diff:
            min_diff = arr[j]-arr[i]

        # Else do not change min_diff
    
    return min_diff

if __name__=='__main__':
    test_cases = [[7, 3, 2, 4, 9, 12, 56], [3, 4, 1, 9, 56, 7, 9, 12],
                [12, 4, 7, 9, 2, 23, 25, 41, 
30, 40, 28, 42, 30, 44, 48, 
43, 50]]
    m = [3, 5, 7]

    for i in range(len(test_cases)):
        result = solution(test_cases[i], m[i])

        print('Case {}:'.format(i+1), end='')
        print(result)