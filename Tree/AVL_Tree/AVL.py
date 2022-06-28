import QueueLinkedList as queue

class AVLNode:
    # Initialization
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1 # for balancing tree (as main purpose of AVL)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data) # root node
    preOrderTraversal(rootNode.leftChild) # left subtree
    preOrderTraversal(rootNode.rightChild) # right subtree

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild) # left subtree
    print(rootNode.data) # root node
    inOrderTraversal(rootNode.rightChild) # right subtree

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild) # left subtree
    postOrderTraversal(rootNode.rightChild) # right subtree
    print(rootNode.data) # root node

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)

            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print('The value is found')
    elif nodeValue < rootNode.data:
        if rootNode.leftChild == nodeValue:
            print('The value is found')
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild == nodeValue:
            print('The value is found')
        else:
            searchNode(rootNode.rightChild, nodeValue)

# helper methods
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def rightRotate(disbalanceNode):
    # using algorithm for right rotation
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode

    # updating height of disbalanceNode and newRoot
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))

    return newRoot

def leftRotate(disbalanceNode):
    # using algorithm for left rotation
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode

    # updating height of disbalanceNode and newRoot
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

# main method

def insertNode(rootNode, nodeValue):
    # CASE-1 (No rotation required)
    # No node present then make the first inserting node as the root node
    if not rootNode:
        return AVLNode(nodeValue)
    # else do comparison and insert the values (similar as in BST)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    # updating height
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))

    # CASE-2 (Rotation required)
    # so before going for the conditions get the balance so that we can decide which rotation is to be performed
    balance = getBalance(rootNode)

    # CONDITION-1 (LL -> Left Left Rotation)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    
    # CONDITION-2 (LR -> Left Right Rotation)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        # first do left rotation and update leftChild of root
        rootNode.leftChild = leftRotate(rootNode.leftChild)

        # second do right rotation and balance the tree
        return rightRotate(rootNode)
    
    # CONDITION-3 (RR -> Right Right Rotation)
    # for right side we are going to check balance < -1 or not (as left-right is the actual formula)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    
    # CONDITION-4 (RL -> Right Left Rotation)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        # first do right rotation and update the rightchild of the current parent node
        rootNode.rightChild = rightRotate(rootNode.rightChild)

        # second do left rotation and balance the tree
        return leftRotate(rootNode)
    
    return rootNode

# helper function to find successor node for the case of deletingNode having two children
def getMinValueNode(rootNode):

    # as the lowest node is always present in the left subtree
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

# main method of deletion
def deleteNode(rootNode, nodeValue):
    # When no rotation required then it works like normal BST conditions
    # In case of rootNode is None
    if not rootNode:
        return rootNode
    # otherwise go for subtrees on the basis of comparison
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    
    # when one or two child present on the deletingNode
    else:
        # when only one child present
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        # when two child present
        # then getting successor present in the right subtree of the deletingNode
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data # changing value of deletingNode to successorNode
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data) # deleting successorNode

    # When rotation required
    # updating height of rootNode
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    # now conditions come
    # LL (Left Left) condition
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    
    # RR (Right Right) condition
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)

    # LR (Left Right) condition
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        # first do left rotate and then right rotate
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    
    # RL (Right Left) condition
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        # first do right rotate and then left rotate
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode

# delete entire AVL tree
def deleteAVL(rootNode):
    # NOTE: Delete rootNode and automatically other nodes will be deleted same as BST.
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The AVL tree has been successfully deleted.'

newAVL = AVLNode(5) # Creation of AVL Tree

# inserting nodes
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
# newAVL = deleteNode(newAVL, 15)
print(deleteAVL(newAVL))
levelOrderTraversal(newAVL)