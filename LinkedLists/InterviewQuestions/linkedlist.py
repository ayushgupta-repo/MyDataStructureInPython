
from random import randint

# Creating node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    # Below is invoked when print or str is called
    def __str__(self):
        return str(self.value)

# Creating LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # For iteration
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # For printing linkedlist
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    # For getting length of linkedlist
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        
        return result

    # Creating insertion for only one case (Insertion at last)
    def add(self, value):
        # When no element/node present
        if self.head is None:
            # Creating newNode
            newNode = Node(value)
            self.head = newNode # connecting head and newNode
            self.tail = newNode # connecting tail and newNode
        # Otherwise when more than one element present
        else:
            self.tail.next = Node(value) # connecting lastNode next to newNode
            self.tail = self.tail.next # connecting tail to current lastNode

    # Generate linked list with random numbers
    def generate(self, n, min_value, max_value):

        # disconnecting head and tail if any element exist previously and creating new list
        self.head = None 
        self.tail = None

        for i in range(n):
            self.add(randint(min_value, max_value))
        
        return self

# # Checking
# customLL = LinkedList()

# customLL.generate(10, 0, 99)

# print(customLL)
# print(len(customLL))