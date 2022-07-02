def setZeros(matrix):
	# Write your code here.
    location = []
    
    # finding location and saving it for further use
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                location.append((i, j))
                
    # complete row making zero
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for each in location:
                if i == each[0]:
                    matrix[i][j] = 0
    
    # for making col zero
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for each in location:
                if j == each[1]:
                    matrix[i][j] = 0
                            
    return matrix

# print(setZeros([[7, 19, 3], [4, 21, 0]]))

print(setZeros([[28, 4, 81, 24, 95], [0, 53, 48, 39, 35], [89, 52, 99, 16, 23], [14, 0, 0, 4, 16 ]]))