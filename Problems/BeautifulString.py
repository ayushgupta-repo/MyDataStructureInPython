def isBeautiful(str):
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            return False
    return True
                        
def makeBeautiful(str):
	# Write your code here

    if isBeautiful(str) == True:
        return 0
    else:
        count = 0
        
        first = str[0]
        
        for i in range(1, len(str)):
            if (i%2 == 0):
                if str[i] != first:
                    count += 1
            else:
                if first == '0':
                    if str[i] != '1':
                        count += 1
                else:
                    if str[i] != '0':
                        count += 1
    return count

test_cases = ['01010010101']

for test in test_cases:
    print(makeBeautiful(test))