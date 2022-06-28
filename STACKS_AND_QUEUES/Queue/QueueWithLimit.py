# CASE-2 Queue using python list with size limit or Circular Queue

class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top+1 == self.start:
            return True
        elif self.start == 0 and self.top+1 == self.maxSize:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def enqueue(self, value):
        if self.isFull():
            return 'The Queue is full'
        else:
            # In case of top pointer is pointing last cell
            if self.top+1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                # Checks if start is -1 then update it to 0
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return 'The element is inserted at the end of Queue'
    
    def dequeue(self):
        if self.isEmpty():
            return 'There is no any element in the Queue'
        else:
            firstElement = self.items[self.start]
            start = self.start
            
            # In case of last element
            if self.start == self.top:
                self.start = -1
                self.top = -1
            # In case of start pointer is at last
            elif self.start+1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return 'There is no any element in the Queue'
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.top = -1

customQueue = Queue(3)
print(customQueue.isEmpty())

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.isEmpty())
print(customQueue)

print(customQueue.isFull())
print(customQueue.peek())

print(customQueue.dequeue())
print(customQueue.peek())
print(customQueue)

customQueue.delete()
print(customQueue)