class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # For printing
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

            # Checking that lastNode next reference is the head or not (to avoid infinite loop)
            if node == self.head:
                break

    # Create CSLL
    def createCSLL(self, value):
        node = Node(value)
        node.next = node # linking to itself as only one element is yet created
        self.head = node
        self.tail = node

        return 'The CSLL is created.'
    
    # For Insertion operation
    def insertCSLL(self, value, location):
        # Check for existence of Circular Singly Linked List
        if self.head is None:
            return 'The CSLL does not exist.'
        else:
            # Create new node
            newNode = Node(value)
            # CASE-I (Insertion at the beginning)
            if location == 0:
                newNode.next = self.head # linking newNode and head
                self.head = newNode # disconnecting head from firstNode and connecting to the newNode
                self.tail.next = newNode # disconnecting lastNode from firstNode and connecting lastNode to newNode
            
            # CASE-II (Insertion at the last)
            elif location == 1:
                newNode.next = self.tail.next # connecting firstNode and the newNode
                self.tail.next = newNode # disconnecting lastNode and firstNode and also connecting lastNode and newNode
                self.tail = newNode # disconnecting tail and lastNode and connecting tail to the newNode
            
            # CASE-III (Insertion at any location)
            else:
                tempNode = self.head
                index = 0
                
                # Doing traversal
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                
                nextNode = tempNode.next
                tempNode.next = newNode # linking currentNode next reference to newNode
                newNode.next = nextNode # linking newNode next reference to the currentNode next reference(nextNode)

    # Traversing the linked list
    def traversalCSLL(self):
        # Checking the existence of CSLL
        if self.head is None:
            print('The CSLL does not exist.')
        else:
            tempNode = self.head

            # traversing through the nodes and printing the value
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

                # Checking is done to prevent the infinite loop
                if tempNode == self.tail.next:
                    break

    # Searching particular value in CSLL
    def searchCSLL(self, nodeValue):
        # Checking the existence of CSLL
        if self.head is None:
            return 'The CSLL does not exist.'
        else:
            tempNode = self.head # tempNode is the currentNode

            # traversing through the nodes to check the value
            while tempNode:
                # checking 2 conditions
                # First condition is currentNode.value==nodeValue
                if tempNode.value == nodeValue:
                    return tempNode.value

                tempNode = tempNode.next
                
                # Second condition to prevent infinite loop that the currentNode is not the head
                if tempNode == self.tail.next:
                    return 'The provided node value does not exist.'

    # Delete node a from CSLL
    def deleteNode(self, location):
        # Checking the existence of CSLL
        if self.head is None:
            print('The CSLL does not exist')
        # Otherwise
        else:
            # CASE-1 (Deletion at beginning)
            if location == 0:
                # CONDITION-1 (When only one node present)
                # Creating condition that if head and tail refers to the same node it means it is the only node present in the CSLL
                if self.head == self.tail:
                    self.head.next = None # disconnecting node that is refering to itself
                    self.head = None # disconnecting head and node
                    self.tail = None # disconnecting tail and node
                
                # CONDITION-2 (When more than one node present)
                else:
                    self.head = self.head.next # disconnecting head and firstNode and connecting head to next of firstNode
                    self.tail.next = self.head # disconnecting lastNode reference with firstNode and connecting lastNode to next of firstNode
            
            # CASE-2 (Deletion at last)
            elif location == -1:
                # CONDITION-1 (When only one node present)
                # Creating condition that if head and tail refers to the same node it means it is the only node present in the CSLL
                if self.head == self.tail:
                    self.head.next = None # disconnecting node that is refering to itself
                    self.head = None # disconnecting head and node
                    self.tail = None # disconnecting tail and node
                
                # CONDITION-2 (When more than one node present)
                else:
                    # Traverse to reach node before lastNode
                    tempNode = self.head
                    while tempNode is not None:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    
                    # tempNode is currNode here
                    # disconnecting and connecting operation done below
                    tempNode.next = self.head
                    self.tail = tempNode

            # CASE-3 (Delete at any location)
            else:
                # Doing traversal to reach node before deletingNode
                tempNode = self.head
                index = 0

                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1

                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # Delete entire CSLL
    def deleteEntireCSLL(self):
        # Checking the existence of CSLL
        if self.head is None:
            print('The CSLL does not exist.')
        # Otherwise
        else:
            self.head = None
            self.tail.next = None
            self.tail = None

circularCSLL = CircularSinglyLinkedList()

print(circularCSLL.createCSLL(1))

# print([node.value for node in circularCSLL])

circularCSLL.insertCSLL(0,0) # CASE-I
circularCSLL.insertCSLL(1,1) # CASE-II
circularCSLL.insertCSLL(2,1) 
circularCSLL.insertCSLL(5,2) # CASE-III

print([node.value for node in circularCSLL])

# circularCSLL.traversalCSLL()
# print(circularCSLL.searchCSLL(1)) # Returns 1
# print(circularCSLL.searchCSLL(9)) # Returns 'The provided node value does not exist'

# circularCSLL.deleteNode(0) # CASE-1
# print([node.value for node in circularCSLL])

# circularCSLL.deleteNode(-1) # CASE-2
# print([node.value for node in circularCSLL])

# circularCSLL.deleteNode(1) # CASE-3
# print([node.value for node in circularCSLL])

circularCSLL.deleteEntireCSLL()
print([node.value for node in circularCSLL])