# Linear Search

def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
        
    return -1

print(linearSearch([2, 32, 64, 1, 5], 5)) # returns 4