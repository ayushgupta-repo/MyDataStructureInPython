# In this output must be elements between first and last element

def middle(lst):
    new = lst[1:]
    del new[-1]
    return new

test_cases = [[-2,1,-3,4,-1,2,1,-5,4], [5,4,-1,7,8]]

for i in range(len(test_cases)):
    result = middle(test_cases[i])

    print('Output for Test Case {}:'.format(i+1), end=' ')
    print(result)