# CASE-1 Queue using python list with no size limit

class Queue:
    def __init__(self):
        self.items = [] # creating list
    
    # for printing
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)

        # NOTE: It's time complexity will be 'Amortized Constant' because after default max size we need to allocate memory for further enqueue operations and this cosumes time in worst case it can be O(n^2)

        return 'The element is inserted at the end of the queue'

    def dequeue(self):
        # Checking elements present or not
        # NOTE: Also in this time complexity is O(n) as in pop operation from beginning shifting of other values is needed
        if self.isEmpty():
            return 'There is no element present in the queue'
        else:
            return self.items.pop(0) # 0 is passed to pop first element

    def peek(self):
        # Checking elements present or not
        if self.isEmpty():
            return 'There is no element present in the queue'
        else:
            return self.items[0]

    def delete(self):
        self.items = []

customQueue = Queue()

# print(customQueue.isEmpty())

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)

print(customQueue.isEmpty())
print(customQueue)

print(customQueue.peek())

print(customQueue.dequeue())
print(customQueue)

print(customQueue.peek())

customQueue.delete()
print(customQueue)