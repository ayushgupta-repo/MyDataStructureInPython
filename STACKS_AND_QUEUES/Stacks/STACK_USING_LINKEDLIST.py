# Creating stack and operations based on linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # for iteration
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.Linkedlist = LinkedList()
    
    # for printing
    def __str__(self):
        values = [str(x.value) for x in self.Linkedlist]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.Linkedlist.head == None:
            return True
        else:
            return False
    
    def push(self, value):
        node = Node(value)
        # connecting newNode to current head and head reference to newNode
        node.next = self.Linkedlist.head # connecting newNode next reference to the head
        self.Linkedlist.head = node # connecting head to the newNode

    def pop(self):
        # Check stack is empty
        if self.isEmpty():
            return 'There is not any element in the stack'
        else:
            # connecting head to next of firstNode
            nodeValue = self.Linkedlist.head.value # storing deleting value
            self.Linkedlist.head = self.Linkedlist.head.next # connecting head to the next of current head
            return nodeValue

    def peek(self):
        # Check stack is empty
        if self.isEmpty():
            return 'There is not any element in the stack'
        else:
            nodeValue = self.Linkedlist.head.value # storing value
            return nodeValue

    def delete(self):
        self.Linkedlist.head = None # disconnecting head with nodes

customStack = Stack()

# print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)

print(customStack.pop())
print(customStack.isEmpty())
print(customStack)

print(customStack.peek())
