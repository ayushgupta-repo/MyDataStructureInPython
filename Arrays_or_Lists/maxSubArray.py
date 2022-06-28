
def findMaxSum(nums):
    result = [0 for i in range(len(nums))]
    sumUpto = [0 for i in range(len(nums))]
    sumUpto[0] = nums[0]
    for i in range(1,len(nums)):
        if sumUpto[i-1] >= 0:
            sumUpto[i] = nums[i] + sumUpto[i-1]
        else:
            sumUpto[i] = nums[i]
    result[0] = nums[0]
    for i in range(1,len(nums)):
        result[i] = max(result[i-1],sumUpto[i])
    return result[-1]
    # biggest = 0
    # sum = 0

    # for num in test:
    #     sum += num
    
    # biggest = sum

    # mid_element_index = len(test)//2

    # while biggest <= sum:


    # return biggest


test_cases = [[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8]]

for i in range(len(test_cases)):
    result = findMaxSum(test_cases[i])

    print('Output for Test Case {}:'.format(i+1), end=' ')
    print(result)