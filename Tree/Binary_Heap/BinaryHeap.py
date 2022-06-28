
# NOTE: There are two ways to implement Binary Heap one is using list and another using reference/pointer
# But using list is most appropriate over here
# And list will be size limit to achieve less space.

class BinaryHeap:
    def __init__(self, size):

        # NOTE: We are creating customList with one larger size as we will avoid index 0 to reduce math calculations
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

def peekofHeap(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1] # as first node contains the peek of the tree

def sizeofHeap(rootNode):
    if not rootNode:
        return
    return rootNode.heapSize # as it contains how much cells in the customList are filled and unfilled will not be counted

# NOTE: There are 4 traversals as learned earlier in Binary Tree but we are using levelOrderTraversal
# So to recall other 3 traversals see that directory

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        # NOTE: We are starting from 1 as 0 is empty and adding 1 to heapSize so as to include last filled index
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])

# Insertion method
# helper method to maintain the tree

# NOTE: passing index as the location of inserted node so as to check the tree is maintained/followed the property of Binary Heap or not
def heapifyTreeInsert(rootNode, index, heapType):
    # getting parent Index
    parentIndex = int(index/2) # as to get childNode we use index*2

    # As index reaching rootNode no comparison remained also tree is maintained
    if index <= 1:
        return

    # now on the basis of heapType we maintain the tree
    if heapType == 'Min':
        # Checking childNode to its parentNode and maintaining the tree
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            # do swapping
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        
        # recursive calling for further above table maintenance but now the index will be the parentIndex as the insertedNode is reached to its parent position
        heapifyTreeInsert(rootNode, parentIndex, heapType)

    if heapType == 'Max':
        # Checking childNode to its parentNode and maintaining the tree
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            # do swapping
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        
        # recursive calling for further above table maintenance
        heapifyTreeInsert(rootNode, parentIndex, heapType)

# main insertion method
def insertNode(rootNode, nodeValue, heapType):
    # If tree is full
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return 'The Binary Heap is full'
    # otherwise if any cell that is unfilled remains insert node other there

    rootNode.customList[rootNode.heapSize+1] = nodeValue # inserting node
    rootNode.heapSize += 1 # incrementing heapSize as node is inserted
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType) # to maintain tree
    return 'The value has been successfully inserted.'

# helper method for extraction of node
def heapifyTreeExtract(rootNode, index, heapType):
    # getting left and right indexes
    leftIndex = index*2
    rightIndex = index*2+1
    swapChild = 0 # to store index of the child which will swap

    # If no child present
    if rootNode.heapSize < leftIndex:
        return

    # In case of one child present (it must be at leftIndex)
    elif rootNode.heapSize == leftIndex:
        # Do operation on the basis of heapType
        if heapType == 'Min':
            # do comparison
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                # do swapping
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return

        # in case of heap type is Max
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                # do swapping
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    
    # In case of two child present
    else:
        # then first decide which child will swap and then perform operation
        if heapType == 'Min':
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            # do comparison between child and parent node
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                # do swapping
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        # if heapType is Max
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            # do comparison
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                # do swapping
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp

# main method
def extractNode(rootNode, heapType):
    # if no node present
    if rootNode.heapSize == 0:
        return
    # otherwise
    else:
        extractedNode = rootNode.customList[1] # extracted node is present as rootNode
        # replace rootNode(index 1) with lastNode(with heapSize)
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None # removing lastNode
        rootNode.heapSize -= 1 # decrementing heapSize as lastNode is removed
        heapifyTreeExtract(rootNode, 1, heapType) # passing 1 as maintenance will start from rootNode 
        return extractedNode

def deleteEntireHeap(rootNode):
    rootNode.customList = None
    return 'The entire Binary Heap has been successfully deleted.'

newBinaryHeap = BinaryHeap(5)

# print(sizeofHeap(newBinaryHeap)) # returns 0 as no elements inserted yet

insertNode(newBinaryHeap, 4, 'Max')
insertNode(newBinaryHeap, 5, 'Max')
insertNode(newBinaryHeap, 2, 'Max')
insertNode(newBinaryHeap, 1, 'Max')

# print(extractNode(newBinaryHeap, 'Max'))

levelOrderTraversal(newBinaryHeap)

print(deleteEntireHeap(newBinaryHeap))
