from os import *
from sys import *
from collections import *
from math import *
from itertools import permutations

from os import *
from sys import *
from collections import *
from math import *
from itertools import permutations

def pairSum(arr, s):
    # Write your code here.
    possibilities = permutations(arr, 2)
    result = []
    
    for each in possibilities:
        if each[0]+each[1] == s:
            result.append([each[0], each[1]])
            
    left_marker = 0
    right_marker = len(result)-1
    
    final_result = []

    for r in result:
        r.sort()

    # get repeated ones
    while left_marker <= right_marker:
        if result[left_marker][0] == result[right_marker][0] and result[left_marker][1] == result[right_marker][1]:
            if result[left_marker] not in final_result:
                final_result.append(result[left_marker])
                left_marker += 1
                right_marker -= 1
            elif result[left_marker] in final_result:
                final_result.append(result[left_marker])
                left_marker += 1
                right_marker -= 1
            else:
                left_marker += 1
                right_marker -= 1
        
    final_result.sort()
    return final_result

print(pairSum([1,2,3,4,5], 5))

print(pairSum([2, -3, 3, 3, -2], 0))