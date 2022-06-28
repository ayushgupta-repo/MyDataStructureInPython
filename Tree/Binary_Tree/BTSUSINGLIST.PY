# Creating Binary Tree using Python List

from distutils.sysconfig import customize_compiler


class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None] # Creating list or fixed size with each cell initial values as None
        self.lastUsedIndex = 0 # as we ignore 0th index and start from 1
        self.maxSize = size

    def insertNode(self, value):
        # Checking if BT is full
        if self.lastUsedIndex + 1 == self.maxSize:
            return 'The Binary Tree is full'
        # Otherwise
        self.customList[self.lastUsedIndex+1] = value # inserting value
        self.lastUsedIndex += 1 # incrementing the index value

        return 'The node is successfully inserted in Binary Tree'

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return 'Success'
        return 'Not Found'
    
    # passing index as parameter to get trace of current location
    def preOrderTraversal(self, index):
        
        # checking that tracing to reach to end or not (stopping condition)
        if index > self.lastUsedIndex:
            return
        
        print(self.customList[index])

        # recursion calls
        self.preOrderTraversal(index*2) # for leftChild
        self.preOrderTraversal(index*2 + 1) # for rightChild

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        
        self.inOrderTraversal(index*2) # for leftChild
        print(self.customList[index]) # for root
        self.inOrderTraversal(index*2+1) # for rightChild

    def postOrderTraversal(self, index):
        # stopping condition
        if index > self.lastUsedIndex:
            return
        
        self.postOrderTraversal(index*2) # for leftChild
        self.postOrderTraversal(index*2+1) # for rightChild
        print(self.customList[index]) # for root

    def levelOrderTraversal(self, index):
        
        # in below condition to include last index we used +1
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return 'There is no any node present in BT'
        # for +1 same as above method reason
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex] # updating the deletingNode value to the lastNode value
                self.customList[self.lastUsedIndex] = None # setting lastNode to None
                self.lastUsedIndex -= 1 # updating the lastUsedIndex value as last node is deleted

                return 'The node is successfully deleted'

    def deleteBT(self):
        # setting customList to None all nodes will be deleted one by one
        self.customList = None
        return 'The BT is successfully deleted'


newBT = BinaryTree(8)
newBT.insertNode('Drinks')
newBT.insertNode('Hot')
newBT.insertNode('Cold')
newBT.insertNode('Tea')
newBT.insertNode('Coffee')

# print(newBT.searchNode('Cola')) # Not Found
# newBT.preOrderTraversal(1) # as 0 is empty so start from 1
# newBT.inOrderTraversal(1) # as 0 is empty so start from 1
# newBT.postOrderTraversal(1) # as 0 is empty so start from 1
# newBT.levelOrderTraversal(1) # as 0 is empty so start from 1

# print(newBT.deleteNode('Hot'))
# newBT.levelOrderTraversal(1) # as 0 is empty so start from 1

print(newBT.deleteBT())
newBT.levelOrderTraversal(1) # as 0 is empty so start from 1