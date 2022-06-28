# Over here we are creating Binary Search Tree (Binary tree with implicit structure such that left subtree will be smaller or equal to parent node and right subtree will be larger than the parent node)

# importing queue for levelOrderTraversal
from requests import delete
import QueueLinkedList as queue

# creating BSTNode class to create/initialize BST

from logging import root


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# creating operations to be performed on BST
def insertNode(rootNode, nodeValue):
    # If no element present then create insertingNode as rootNode
    if rootNode.data is None:
        rootNode.data = nodeValue

    # If more elements
    # Otherwise comparing the value to go right/left
    # to go left subtree side
    elif nodeValue <= rootNode.data:
        # Checking that current parent node's leftChild is None so insert directly if not then traverse by calling recursively
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        # Otherwise traversing left side by recursively calling
        else:
            insertNode(rootNode.leftChild, nodeValue)
        
    # to go right subtree side
    else:
        # checking that current parent's rightChild is none or not
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        # Otherwise traversing right side
        else:
            insertNode(rootNode.rightChild, nodeValue)

    return 'The node is successfully inserted'

def preOrderTraversal(rootNode):
    # checking if BST exist
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

    # ONE WAY
    # if not rootNode:
    #     return 
    # else:
    #     customQueue = queue.Queue()
    #     customQueue.enqueue(rootNode)

    #     while not(customQueue.isEmpty()):
    #         root = customQueue.dequeue()

    #         if root.value.data == nodeValue:
    #             return 'Successfully found'
            
    #         # traversing left subtree on the basis of comparison
    #         elif nodeValue < root.value.data:
    #             if root.value.leftChild is not None:
    #                 customQueue.enqueue(root.value.leftChild)
    #             else:
    #                 return 'Not found'
            
    #         else:
    #             if root.value.rightChild is not None:
    #                 customQueue.enqueue(root.value.rightChild)
    #             else:
    #                 return 'Not found'

    # SECOND WAY
    # NOTE: For second way it shows error in case of not founding the value
    if rootNode.data == nodeValue:
        print('The value is found')
        return
    
    # going for comparison
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print('The value is found')
        else:
            # recursive call
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print('The value is found')
        else:
            # recursive call
            searchNode(rootNode.rightChild, nodeValue)

# helper method to found successor in case of deletion operation in case of two children present
def minValueNode(bstNode):
    current = bstNode

    # as lowest value is present in the left subtree from any parent node
    while (current.leftChild is not None):
        current = current.leftChild # traversing left side
    
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    
    # going for left subtree
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    
    # going for right subtree
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    
    # if node found
    else:

        # For one child case
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        # if two children present
        temp = minValueNode(rootNode.rightChild) # getting successor
        rootNode.data = temp.data # replacing the values
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data) # now deleting the successor from it's previous position and updating the rightChild
    
    return rootNode

def deleteBST(rootNode):
    # deleting root node will delete other node automatically
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The BST has been successfully deleted'


            

newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)

# to check that the nodes are successfully inserted
# print(newBST.data)
# print(newBST.leftChild.data)
# print(newBST.rightChild.data)

# preOrderTraversal(newBST)
# inOrderTraversal(newBST)
# postOrderTraversal(newBST)
# levelOrderTraversal(newBST)

# searchNode(newBST, 100)

# levelOrderTraversal(newBST)
# deleteNode(newBST, 100)
# levelOrderTraversal(newBST)

print(deleteBST(newBST))
levelOrderTraversal(newBST)