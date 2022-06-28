# creating node class
from platform import node


class Node:
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.head = None
        self.tail = None

# creating CircularDoublyLinkedList (CDLL) class
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # for printing
    def __iter__(self):
        # do traversal and return each node value
        node = self.head
        while node:
            yield node
            node = node.next
            
            # checking that the next reference of the node (curNode) is head or not to prevent infinite loop
            if node == self.tail.next:
                break
    
    # creating CDLL
    def createCDLL(self, nodeValue):
        # creating newNode with provided by value
        newNode = Node(nodeValue)

        # connecting and disconnecting operations
        self.head = newNode # connecting head to newNode
        self.tail = newNode # connecting tail to newNode
        newNode.next = newNode # connecting next reference of newNode to itself as that is the only node present in CDLL
        newNode.prev = newNode # connecting prev reference of newNode to itself as that is the only node present in CDLL

        return 'The CDLL is created successfully.'

    # Insertion method in CDLL
    def insertCDLL(self, nodeValue, location):
        # Checking existence of CDLL
        if self.head is None:
            return 'The CDLL does not exist.'
        # Otherwise
        else:
            # Creating newNode
            newNode = Node(nodeValue)

            # CASE-1 (Insertion at first)
            if location == 0:
                newNode.next = self.head # connecting newNode next reference to the firsNode (that is head now)
                newNode.prev = self.head.prev # connecting newNode prev reference to the lastNode (that can be referred by firstNode prev reference)
                self.head.prev = newNode # connecting prev reference of firstNode to newNode
                self.head = newNode # connecting head to newNode and making it firstNode
                self.tail.next = newNode # connecting lastNode next reference to newNode

            # CASE-2 (Insertion at last)
            elif location == -1:
                newNode.next = self.tail.next # connecting newNode next reference to firstNode (that is lastNode next reference)
                newNode.prev = self.tail # connecting newNode prev reference to lastNode
                self.tail.next = newNode # connecting lastNode next reference to newNode
                self.tail = newNode # connecting tail to newNode and making it lastNode
                self.head.prev = newNode # connecting firstNode prev reference to newNode
            
            # CASE-3 (Insertion at specified location)
            else:
                # Do traversal and stop at node before the inserting location
                tempNode = self.head
                index = 0
                
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                
                # tempNode is curNode here
                newNode.next = tempNode.next # connecting newNode next reference to the curNode next reference
                newNode.prev = tempNode # connecting newNode prev reference to the curNode
                newNode.next.prev = newNode # connecting prev of next of curNode to the newNode
                tempNode.next = newNode # connecting curNode next reference to the newNode

    # Traversal from head to tail for CDLL
    def traversalCDLL(self):
        # Note: Always check that the curNode is the tail or not to prevent infinite loop scenario
        
        # Checking existence of CDLL
        if self.head is None:
            print('There is no any node for traversal in CDLL')

        # Otherwise
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
    
    # Reverse Traversal from tail to head for CDLL
    def reverseTraversalCDLL(self):
        # Note: Always check that the curNode is head or not to prevent infinite loop scenario
        
        # Checking existence of CDLL
        if self.head is None:
            print('There is no any node for reverse traversal in CDLL')
        
        # Otherwise
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev
    
    # Search value from CDLL
    def searchCDLL(self, nodeValue):
        # Checking existence of CDLL
        if self.head is None:
            return 'No any element present in CDLL'
        # Otherwise
        else:
            # Do traversal and find the value
            curNode = self.head
            while curNode:
                if curNode.value == nodeValue:
                    return curNode.value
                
                # Checking that curNode is the lastNode or not
                if curNode == self.tail:
                    return 'The value does not exist in CDLL'

                curNode = curNode.next

    # Delete node from CDLL
    def deleteNode(self, location):
        # Checking existence of CDLL
        if self.head is None:
            print('There is no any node to delete.')
        # Otherwise
        else:
            # CASE-1 (Deletion from first)
            if location == 0:
                # CONDITION-1 (Only one node)
                if self.head == self.tail:
                    self.head.next = None # disconnecting next reference of the only node that was set to itself
                    self.head.prev = None # disconnecting prev reference of the only node that was set to itself
                    self.head = None # disconnecting head and the node
                    self.tail = None # disconnecting tail and the node
                
                # CONDITION-2 (More than one node)
                else:
                    self.head = self.head.next # connecting head to the next of the firstNode
                    self.head.prev = self.tail # connecting curHead prev reference to the tail
                    self.tail.next = self.head # connecting lastNode next reference to the curHead
            
            # CASE-2 (Deletion from last)
            elif location == -1:
                # CONDITION-1 (Only one node)
                if self.head == self.tail:
                    self.head.next = None # disconnecting next reference of the only node that was set to itself
                    self.head.prev = None # disconnecting prev reference of the only node that was set to itself
                    self.head = None # disconnecting head and the node
                    self.tail = None # disconnecting tail and the node
                
                # CONDITION-2 (More than one node)
                else:
                    self.tail = self.tail.prev # connecting tail to the prev reference of the lastNode
                    self.tail.next = self.head # connecting curTail next reference to the head
                    self.head.prev = self.tail # connecting prev reference of the head to the curTail
            
            # CASE-3 (Deletion from specified location)
            else:
                # Do traversal and reach the node before the deletingNode location
                curNode = self.head
                index = 0

                while index < location - 1:
                    index += 1
                    curNode = curNode.next

                curNode.next = curNode.next.next # connecting next reference of curNode to the next of the deletingNode
                curNode.next.prev = curNode # connecting prev reference of the next of curNode to the curNode

    # Delete entire CDLL
    def deleteCDLL(self):
        # Checking existence of CDLL
        if self.head is None:
            print('The CDLL does not exist')
        # Otherwise
        else:
            # disconnect and also do traversal and set prev reference of each node to null
            curNode = self.head
            self.tail.next = None # disconnecting lastNode and firstNode
            while curNode:
                curNode.prev = None # disconnecting each node prev reference to null
                curNode = curNode.next
            
            self.head = None # disconnecting head and firstNode
            self.tail = None # disconnecting tail and lastNode
            print('CDLL deleted successfully')

circularDLL = CircularDoublyLinkedList()

# creating CDLL
print(circularDLL.createCDLL(1))

# printing
# print([node.value for node in circularDLL])

# checking insertion
circularDLL.insertCDLL(0,0) # CASE-1
circularDLL.insertCDLL(2,-1) # CASE-2
circularDLL.insertCDLL(3,1) # CASE-3

print([node.value for node in circularDLL])

# checking traversal
# circularDLL.traversalCDLL()
# circularDLL.reverseTraversalCDLL()

# print(circularDLL.searchCDLL(9))

# Checking Deletion
# circularDLL.deleteNode(0) # CASE-1
# print([node.value for node in circularDLL])

# circularDLL.deleteNode(-1) # CASE-2
# print([node.value for node in circularDLL])

# circularDLL.deleteNode(2) # CASE-3
# print([node.value for node in circularDLL])

# Checking deletion of entire CDLL
circularDLL.deleteCDLL()
print([node.value for node in circularDLL])