# creating Node class
from platform import node


class Node:
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.prev = None
        self.next = None

# creating DoublyLinkedList class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # for printing purpose
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # creating DoublyLinkedList(DLL)
    def createDLL(self, nodeValue):
        # creating newNode
        node = Node(nodeValue)

        # connecting and disconnecting operation
        node.next = None
        node.prev = None
        self.head = node # connecting head to newNode as it is the only node
        self.tail = node # connecting tail to newNode as it is the only node

    # insertion in DLL
    def insertNode(self, nodeValue, location):
        # Checking the existence of DLL
        if self.head is None:
            print('The DLL does not exist so the node can not be inserted.')
        # Otherwise
        else:
            # creating newNode
            newNode = Node(nodeValue)

            # CASE-1 (Insertion at the beginning)
            if location == 0:
                newNode.prev = None # set the prev reference of newNode to null as it is going to be the first node
                newNode.next = self.head # connecting newNode next reference to the firstNode
                self.head.prev = newNode # connecting firstNode prev reference to the newNode
                self.head = newNode # refering head to the newNode

            # CASE-2 (Insertion at the last)
            elif location == -1:
                newNode.next = None # set the next reference of newNode to null as it is going to be the lastNode
                newNode.prev = self.tail # connecting prev reference of newNode to the lastNode
                self.tail.next = newNode # connecting next reference of lastNode to the newNode
                self.tail = newNode # refering tail to the newNode

            # CASE-3 (Insertion at any location)
            else:
                # Doing traversal to reach node before the insertion location
                tempNode = self.head
                index = 0

                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                
                # tempNode is currNode here

                newNode.next = tempNode.next # connecting newNode next reference to the next of currNode
                newNode.prev = tempNode # connecting newNode prev reference to the currNode
                tempNode.next.prev = newNode # connecting prev of next of currNode to newNode
                tempNode.next = newNode # connecting tempNode next reference to the newNode

    # Traversal method in DLL
    def traverseDLL(self):
        # Checking the existence of DLL
        if self.head is None:
            print('No any element present in DLL')
        # Otherwise
        else:
            # Traverse and print the nodes from head to tail
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    
    # Reverse Traversal method in DLL
    def revTraverseDLL(self):
        # Checking the existence of DLL
        if self.head is None:
            print('No any element present in DLL')
        # Otherwise
        else:
            # Traverse and printing but now from tail to head
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
    
    # Search element in DLL
    def searchDLL(self, nodeValue):
        # Checking the existence of DLL
        if self.head is None:
            return 'No element present in DLL'
        # Otherwise
        else:
            # Do traversal and search for the value
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return 'Finding value does not exist in DLL'

    # Delete node in DLL
    def deleteNode(self, location):
        # Checking existance of DLL
        if self.head is None:
            print('No elements present in DLL')
        # Otherwise
        else:
            # CASE-1 (Deleting the first node)
            if location == 0:
                # CONDITION-1 (If only one node is present)
                # Making condition like if head and tail both refers to the same node it means it is the only node present in the DLL
                if self.head == self.tail:
                    self.head = None # disconnecting head and the node
                    self.tail = None # disconnecting tail and the node
                
                # CONDITION-2 (If more than one node present)
                else:
                    self.head = self.head.next # connecting head to the secondNode
                    self.head.prev = None # set the prev of the secondNode (right now it is the head) to the null

            # CASE-2 (Deleting the last node)
            elif location == -1:
                # CONDITION-1 (If only one node is present)
                if self.head == self.tail:
                    self.head = None # disconnecting head and the only node
                    self.tail = None # disconnecting tail and the only node
                
                # CONDITION-2 (If more than one node present)
                else:
                    self.tail = self.tail.prev # connecting tail to the prev reference of the lastNode
                    self.tail.next = None # set previous of lastNode (that is currently the lastNode from above code) to the null
            
            # CASE-3 (Deleting any node whose location provided)
            else:
                # Do traversal and stop one node before the deletingNode
                curNode = self.head
                index = 0

                while index < location-1:
                    curNode = curNode.next
                    index += 1
                
                curNode.next = curNode.next.next # connecting curNode next reference to the next of the deletingNode
                curNode.next.prev = curNode # connecting prev reference of the next of the curNode to the curNode

    # Deleting entire DLL method
    def deleteEntireDLL(self):
        # Checking the existence of DLL
        if self.head is None:
            print('No element present in the DLL')
        # Otherwise
        else:
            # CONDITION-1 (Set each node prev reference to null as whenever the nodes refers themselves they never got deleted by the grabage collector)
            # For this we need to do traversal
            tempNode = self.head
            while tempNode:
                tempNode.prev = None # disconnecting prev reference of each node to null
                tempNode = tempNode.next
            
            # CONDITION-2 (Set head and tail to null)
            self.head = None # disconnecting head and the firstNode
            self.tail = None # disconnecting tail and the lastNode

doublyLL = DoublyLinkedList()

doublyLL.createDLL(1)

doublyLL.insertNode(0,0) # CASE-1
doublyLL.insertNode(2,-1) # CASE-2
doublyLL.insertNode(3,1) # CASE-3

print([node.value for node in doublyLL])
# doublyLL.traverseDLL()
# doublyLL.revTraverseDLL()
# print(doublyLL.searchDLL(6))

# doublyLL.deleteNode(0) # CASE-1
# doublyLL.deleteNode(-1) # CASE-2
# doublyLL.deleteNode(2) # CASE-3
# print([node.value for node in doublyLL])

doublyLL.deleteEntireDLL()
print([node.value for node in doublyLL])