# CASE-3: Queue using Linked List
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    def enqueue(self, value):
        # Creating newNode
        newNode = Node(value)

        # CONDITION - 1 (When there is no element present)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        # CONDITION - 2 (When elements present)
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return 'There is no any element present in the Queue'
        else:
            firstElement = self.linkedList.head
            self.linkedList.head = self.linkedList.head.next
            return firstElement
    
    def peek(self):
        if self.isEmpty():
            return 'There is no any element present in the Queue'
        else:
            return self.linkedList.head
    
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None

# customQueue = Queue()
# print(customQueue.isEmpty())

# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(3)
# print(customQueue.isEmpty())
# print(customQueue)

# print(customQueue.peek())

# print(customQueue.dequeue())
# print(customQueue.peek())

# print(customQueue)

# customQueue.delete()
# print(customQueue)