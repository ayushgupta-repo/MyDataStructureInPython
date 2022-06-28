# Creating Binary Tree (Tree in which nodes can have atmost 2 nodes as child nodes) using Linked List

# NOTE: We are using QueueLinkedList file to use Queue and create levelOrderTraversal
import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data

        # initializing references as null
        self.leftChild = None
        self.rightChild = None 
    
newBT = TreeNode('Drinks')
hot = TreeNode('Hot')
cold = TreeNode('Cold')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
# cola = TreeNode('Cola')
# fanta = TreeNode('Fanta')

# joining nodes to it's parents
newBT.leftChild = hot
newBT.rightChild = cold

hot.leftChild = tea
hot.rightChild = coffee

# cold.leftChild = cola
# cold.rightChild = fanta

# creating preOrder Traversal (sequence is like root -> left subtree -> right subtree)
def preOrderTraversal(rootNode):
    # Checking condition
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# preOrderTraversal(newBT)

# creating inOrder Traversal (sequence is like left subtree -> root -> right subtree)
def inOrderTraversal(rootNode):
    # Checking condition
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# inOrderTraversal(newBT)

# creating postOrder Traversal (sequence is like left subtree -> right subtree -> root)
def postOrderTraversal(rootNode):
    # Checking condition
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# postOrderTraversal(newBT)

# creating levelOrder Traversal (sequence is like upper level to lower level and from left to right)
# NOTE: We need to have Queue to store level wise nodes and do operations
def levelOrderTraversal(rootNode):
    # Checking condition
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        # And performing queue operations to store and retrieve binary tree nodes level wise
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)

            # going for the leftChild
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            # going for the rightChild
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

# levelOrderTraversal(newBT)

# creating searchBT using levelOrderTraversal
def searchBT(rootNode, nodeValue):
    # Checking condition
    if not rootNode:
        return 'The BT does not exist'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()

            # Checking if the current root node is the node which we are searching for
            if root.value.data == nodeValue:
                return 'Success'
            
            # going for leftChild element
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            # going for rightChild element
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        
        return 'Not Found'

# print(searchBT(newBT, 'Coffee'))

# creating inserting node in binary tree using levelOrderTraversal
def insertNodeBT(rootNode, newNode):
    # CASE-1 (When no node present)
    # Then create rootNode as the inserting node
    if not rootNode:
        rootNode = newNode
    
    # CASE-2 (When nodes present then go for finding vacant position using levelOrderTraversal and consider left and then right side)
    else:
        customeQueue = queue.Queue()
        customeQueue.enqueue(rootNode)

        while not(customeQueue.isEmpty()):
            root = customeQueue.dequeue()

            # Checking for vacant position in leftChild side (on same level)
            if root.value.leftChild is not None:
                customeQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return 'Successfully inserted'
            
            # Checking for vacant positions in rightChild side (on same level)
            if root.value.rightChild is not None:
                customeQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return 'Successfully inserted'

# newNode = TreeNode('Cola')
# newNode1 = TreeNode('Fanta')

# print(insertNodeBT(newBT, newNode))
# print(insertNodeBT(newBT, newNode1))
# levelOrderTraversal(newBT)

# creating deletion of node in Binary Tree
# NOTE: We can not directly delete node in BT as it's children nodes will also get deleted.
# So, to avoid this we replace the values of deletingNode and the leafNode (on the basis of levelOrderTraversal it will be the last node)
# We need to create total three methods
# Method-1: To get the deepest node
# Method-2: To delete the deepest node
# Method-3: To delete/replace the deletingNode with the deepeseNode

# Method-1: 
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()

            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        
        deepestNode = root.value
        return deepestNode

# Method-2:
def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()

            # Checking if the root node is the deepsetNode
            if root.value is dNode:
                root.value = None
                return
            
            # Checking the right subtree as it can be most probable to contain the deepsetNode
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            
            # Checking the left subtree
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return 'The BT does not exist'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()

            if root.value.data == node:

                # calling helper methods
                dNode = getDeepestNode(rootNode) # to get deepest node (METHOD-1)

                deleteDeepestNode(rootNode, dNode) # to delete deepest node (METHOD-2)

                root.value.data = dNode.data
                return 'The node is successfully deleted from BT'
            
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        
        return 'Failed to delete'

# print(deleteNodeBT(newBT, 'Hot'))
# levelOrderTraversal(newBT)

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The BT is successfully deleted'

# print(deleteBT(newBT))

# levelOrderTraversal(newBT)
            