# Question is like you have to find unique coins based on given coins also
# keep in mind to complete it with time complexity of O(n)

# You can do above question by doing XOR operation among the pair of coins
def findUnique(coins):
    
    i = 0

    while i < len(coins):
        temp = i+1

        if coins[i] != coins[temp+1]:
            temp += 1
        
        




data = [1,2,1,2,5]