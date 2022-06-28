# Question-4: Queue via Stacks
# Implement Queue class which implements a queue using two stacks.
# LOGIC:
# Create two stacks
# Use one for enqueue() and then dequeue() elements from first stack and push it to second stack
# In this way first element gets at the top in second stack
# pop that element and then again do dequeue() of elements from second stack and push it to first stack

class Stack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)
    
    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list.pop()

class QueueViaStacks:
    def __init__(self):
        # Initializing two stacks
        self.inStack = Stack() # stack1
        self.outStack = Stack() # stack2

    def enqueue(self, item):
        self.inStack.push(item)
    
    def dequeue(self):
        # Dequeueing elements from inStack and pushing it to outStack
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        
        result = self.outStack.pop() # storing first enqueued element as it will be at the top in the second stack

        # returning the elements from outStack to inStack
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())

        return result

customQueue = QueueViaStacks()

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)

print(customQueue.dequeue()) # returns 1
print(customQueue.dequeue()) # returns 2