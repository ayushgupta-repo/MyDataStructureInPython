def longestUnivaluePath(root):
    # Write your code here.
    count = [0, 0]
    
    parentIndexForLeft = 0
    parentIndexForRight = 0
    
    for i in range(2, len(root)):
        if i%2 == 0 and root[i] > -1:
            parentIndexForLeft = i//2
            if root[i] == root[parentIndexForLeft]:
                count[0] += 1
        if i%2 != 0 and root[i] > -1:
            parentIndexForRight = i//2
            if root[i] == root[parentIndexForRight]:
                if parentIndexForLeft == parentIndexForRight:
                    count[0] += 1
                else:
                    count[1] += 1

    return max(count)+1

if __name__=='__main__':
    print(longestUnivaluePath([0, 7, 7, 7, 8, 3, -1, 7]))