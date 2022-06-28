
def containsDuplicate(nums):
    flag = 0
    nums.sort()
    for i in range(len(nums)-2):
        if nums[i] == nums[i+1]:
            flag = 1
            break

    if flag == 0:
        return False
    else:
        return True

test_cases = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]

for i in range(len(test_cases)):
    result = containsDuplicate(test_cases[i])

    print('Output for Test Case {}:'.format(i+1), end=' ')
    print(result)