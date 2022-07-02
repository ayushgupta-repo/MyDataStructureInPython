
# from itertools import permutations

# def oddToEven(num):
# 	# Write your code here.
    
#     # temp = num
    
#     # numbers = []
    
#     # possibilities = []
    
#     # for i in range(len(temp)-1):
#     #     if int(temp[i])%2 == 0:
#     #         # do swapping
#     #         # temp[i], temp[-1] = temp[-1], temp[i]

#     #         swap_num1 = temp[i]
#     #         swap_num2 = temp[-1]

#     #         new = ''

#     #         for j in range(len(temp)-1):
#     #             if i != j:
#     #                 new += temp[j]
#     #             else:

            
#     #         # append new generated even number
#     #         possibilities.append(temp)
            
#     #         temp = num
            
#     # for i in possibilities:
#     #     numbers.append(int(i))
        
#     # if possibilities is None:
#     #     return -1
#     # else:
#     #     return max(numbers)

#     num = int(num)

#     numbers = []
#     possibilities = []

#     while num >= 10:
#         rem = num%10

#         numbers.append(rem)

#         num = num//10
    
#     numbers.append(num)

#     permuted_numbers = permutations(numbers, len(numbers))

#     return permuted_numbers

#     # for numbers in permuted_numbers:
#     #     if numbers[-1]%2 == 0:
#     #         for n in numbers:

def oddToEven(num):
	# Write your code here.
    
    temp = num
    
    numbers = []
    
    possible = 0
    
    for i in range(len(temp)-1):
        if int(temp[i])%2 == 0:
            possible += 1
    
    possibilities = [[]] * possible
    count = 0
    
    for i in range(len(temp)-1):
        if int(temp[i])%2 == 0:
            # do swapping
            # temp[i], temp[-1] = temp[-1], temp[i]
            
            for j in range(len(temp)):
                possibilities[count].append(temp[j])
                
            # possibilities[count].replace(temp[i], temp[-1])
            # possibilities[count].replace(temp[-1], temp[i])

            # possibilities[count][i] = temp[-1]
            # possibilities[count][-1] = temp[i]
            
#             # append new generated even number
#             possibilites.append(temp)
            swapNum_1 = temp[i]
            swapNum_2 = temp[-1]

            possibles = ''.join(possibilities[0])

            # for possibility in possibilities:
            #     possibility.replace(temp[i], swapNum_2)
            #     possibility.replace(temp[len(temp)-1], swapNum_1)

            possibles = possibles.replace(temp[i], swapNum_2)
            possibles = possibles.replace(temp[len(temp)-1], swapNum_1)


            
            temp = num
            count += 1
            
    # for i in possibilities:
    #     numbers.append(int(i))
        
    # if possibilities is None:
    #     return -1
    # else:
    #     return max(numbers)



    return numbers

num = '652345'
# result = oddToEven(num)

# even = []

# for i in result:
#     if i[-1]%2 == 0 and i[0] == int(num[-1]):
#         even.append(i)

print(oddToEven(num))
                    
            
        