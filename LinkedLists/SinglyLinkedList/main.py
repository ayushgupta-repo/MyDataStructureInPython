class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # For printing
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # For insertion operation
    def insertSLL(self, value, location):
        # Creating new node
        newNode = Node(value)

        # Checking head value for 'None' which means linked list is empty so place the node as the first node in linked list
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        
        # Checking for different conditions based on location provided
        else:

            # Below means insert node at the beginning
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            
            # Below means insert node at the last/end
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode # link created between current last node and the newNode that will be placed at that last location
                self.tail = newNode
            
            # Below for the insertion of node at the particular location between first and last node
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next # travesing is done
                    index += 1
                
                # tempNode is our currentNode
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

                # If the location points to tail then insert at end condition happens
                if tempNode == self.tail:
                    self.tail = newNode

    # For Traversing Singly Linked List
    def traverseSLL(self):
        # Checking for empty/not existing linked list
        if self.head is None:
            print('The Singly Linked List does not exist.')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    # Search for node in Singly Linked List
    def searchSLL(self, nodeValue):
        # Checking for empty/not existing linked list
        if self.head is None:
            print('The Singly Linked List does not exist.')
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return ('The value does not exist in the Singly Linked List')

    # Deleting node in Singly Linked List
    def deleteNode(self, location):
        # Check if the Singly Linked List is empty/not existing
        if self.head is None:
            print('The SLL does not exist.')
        
        # Check for otherwise conditions
        else:
            # Case-I: Deletion of first node
            if location == 0:
                # Condition-I: If only one node present in Singly Linked List
                # Creating condition like when head and tail refers to the same node it means that is the single node present in the SLL
                if self.head == self.tail:
                    self.head = None # Disconnecting node from head
                    self.tail = None # Disconnecting node from tail, now the garbage collector will delete the node automatically
                
                # Condition-II: If more than one node present in SLL
                else:
                    self.head = self.head.next
            
            # Case-II: Deletion of last node
            elif location == 1:
                # Condition-I: If only one node present in Singly Linked List
                # Creating condition like when head and tail refers to the same node it means that is the single node present in the SLL
                if self.head == self.tail:
                    self.head = None # Disconnecting node from head
                    self.tail = None # Disconnecting node from tail, now the garbage collector will delete the node automatically
                
                # Condition-II: If more than one node present in SLL
                else:
                    # We need to do traversal to reach one node before tha last node
                    node = self.head

                    while node is not None:

                        # If the next node of a particular node is also referred by the tail then it means the upcoming node is tha last node
                        if node.next == self.tail:
                            break # Breaking to get the node before the last node
                        
                        node = node.next

                    node.next = None # Disconnecting last and one node previous to last node
                    self.tail = node

            # Case-III: Deleting the node whose location provided 
            else:
                tempNode = self.head
                index = 0

                # Stopping one node before the location of node to be deleted
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # Deleting entire SLL
    def deleteEntireSLL(self):
        # Checking if SLL exist
        if self.head is None:
            print('The SLL does not exist.')
        else:
            self.head = None # Disconnecting head from the node
            self.tail = None # Disconnecting tail from the node

singlyLinkedList = SLinkedList()

# inserting values
# singlyLinkedList.insertSLL(1, 1)
# singlyLinkedList.insertSLL(2, 1)
# singlyLinkedList.insertSLL(3, 1)
# singlyLinkedList.insertSLL(4, 1)
# singlyLinkedList.insertSLL(5,-1)

singlyLinkedList.insertSLL(1, 0)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 2)
singlyLinkedList.insertSLL(4, 3)
singlyLinkedList.insertSLL(5, -1)
singlyLinkedList.insertSLL(0, 3)

# printing values
print([node.value for node in singlyLinkedList])

# traversing and printing the values of nodes
# singlyLinkedList.traverseSLL()

# Searching for the value
# print('The value provided: ',singlyLinkedList.searchSLL(9))

# Deletion of particular node by providing location
# testing every case that I had made
# singlyLinkedList.deleteNode(0) # Case-I
# print([node.value for node in singlyLinkedList])

# singlyLinkedList.deleteNode(1) # Case-II
# print([node.value for node in singlyLinkedList])

# singlyLinkedList.deleteNode(3) # Case-III
# print([node.value for node in singlyLinkedList])

# Deleting the entire SLL
singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])