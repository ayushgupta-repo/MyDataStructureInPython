
# def generatePossibilities(arr, n):
#     if n == 1:
#         return []
#     else:
#         possibilities = [[] for _ in range(n)]
#         for i in range(len(arr)):
#             for j in range(i, len(arr)):
#                 package = [arr[i], arr[j]]

#                 if package not in possibilities[i]:
#                     possibilities[i].append(package)
#         return possibilities

def twoSum(arr, target, n):
    # Write your code here.
    # possibilities = generatePossibilities(arr, n)
    # finalAns = []
    
    # for possibles in possibilities:
    #     for each in possibles:
    #         if each[0] + each[1] == target:
    #             finalAns.append([each[0], each[1]])
    
    # if len(finalAns) == 0:
    #     finalAns.append([-1, -1])
    
    # return finalAns

    # Another Approach:

    if n == 1:
        return [[-1, -1]]

    final = [[] for _ in range(n)]

    for i in range(n):
        rem = target - arr[i]
        for j in range(i, n):
            if rem == arr[j]:
                package = [arr[i], arr[j]]
                if package not in final[i]:
                    final[i].append(package)
    flag = 0

    for each in final:
        if len(each) == 0:
            flag = 0
        else:
            flag = 1
            break

    if flag == 1:
        temp = []

        for i in range(n):
            for j in range(len(final[i])):
                temp.append(final[i][j])
        return temp
    else:
        return [[-1, -1]]
    # if len(final[0]) == 0:
    #     return [-1, -1]
    # for each in final:
    #     each.sort()
    # return final

def takeInput() :

    n, tar = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    return n, tar, arr

def printAns(ans):
    for i in ans:
        if i[0] < i[1]:
            print('{} {}'.format(i[0], i[1]))
        else:
            print('{} {}'.format(i[1], i[0]))

t = int(input().strip())
for i in range(t) :

    # n, target, arr = takeInput()
    # n = 5
    # target = 1
    # arr = [1, -1, -1, 2, 2]
    # # arr = [1,2,3,4,5]

    n = 1
    target = 4
    arr = [2]

    ans = twoSum(arr, target, n)
    # printAns(ans)

    for i in ans:
        print(i)

# n = 1
# target = 4
# arr = [2]

# ans = twoSum(arr, target, n)

# for i in ans:
#     print(i)