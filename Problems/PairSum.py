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
    
    while left_marker != right_marker:
        if result[left_marker][0] == result[right_marker][0] and result[left_marker][1] == result[right_marker][0]:
            if result[left_marker] in final_result:
                continue
            else:
                final_result.append(result.pop(left_marker))
                left_marker = 0
                right_marker = len(result)-1
        else:
            right_marker -= 1
        
    return final_result

pairSum([1,2,3,4,5], 5)