
from sys import stdin

def getProductArrayExceptSelf(arr, n) :
    #Your code goes here
    temp = [i for i in arr]
    
    for i in range(len(arr)):
        arr[i] = 1
        for j in range(len(temp)):
            if i != j:
                arr[i] *= temp[j]
                
    return arr

print(getProductArrayExceptSelf([1,2,3,4,5], 5))