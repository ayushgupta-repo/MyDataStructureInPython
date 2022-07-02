class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex+1 == self.maxSize:
            return 'The BT is full'
        else:
            self.customList[self.lastUsedIndex+1] = value
            self.lastUsedIndex += 1

            return 'The node is successfully inserted'

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)

    def searchNode(self, value):
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return True

        return False

    def findAncestor(self, value1, value2):
        storeParentsFor1 = []
        storeParentsFor2 = []

        if self.searchNode(value1) and self.searchNode(value2):
            locationOfValue1 = self.customList.index(value1)
            locationOfValue2 = self.customList.index(value2)

            while locationOfValue1 >= 1 and locationOfValue2 >= 1:
                locationOfValue1 = locationOfValue1//2
                locationOfValue2 = locationOfValue2//2

                if locationOfValue1 > 0:
                    storeParentsFor1.append(locationOfValue1)
                if locationOfValue2 > 0:
                    storeParentsFor2.append(locationOfValue2)
        
        # return (storeParentsFor1, storeParentsFor2)

        for parentForA in storeParentsFor1:
            for parentForB in storeParentsFor2:
                if parentForA == parentForB:
                    return parentForA


newBT = BinaryTree(10)
# newBT.insertNode('Drinks')
# newBT.insertNode('Hot')
# newBT.insertNode('Cold')
# newBT.insertNode('Tea')
# newBT.insertNode('Coffee')
newBT.insertNode(1)
newBT.insertNode(2)
newBT.insertNode(3)
newBT.insertNode(4)
newBT.insertNode(5)
newBT.insertNode(6)
newBT.insertNode(7)
newBT.insertNode(8)
newBT.insertNode(9)

newBT.inOrderTraversal(1)
print('Common Parent: ', newBT.findAncestor(8, 5))