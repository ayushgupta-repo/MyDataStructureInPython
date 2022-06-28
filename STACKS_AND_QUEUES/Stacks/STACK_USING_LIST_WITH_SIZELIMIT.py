# Creating stack and operations based on python list with size limit

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        # Checking if the list is empty
        if self.list == []:
            return True
        else:
            return False
    
    # isFull
    def isFull(self):
        # Checking length of list to the maxSize
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    # push
    def push(self, value):
        # Checking if stack is full
        if self.isFull():
            return 'The stack is full'
        else:
            self.list.append(value)
            return 'The element has been successfully inserted.'
    
    # pop
    def pop(self):
        # Checking if stack is empty
        if self.isEmpty():
            return 'There is not any element in the stack'
        else:
            return self.list.pop()

    # peek
    def peek(self):
        # Checking if stack is empty
        if self.isEmpty():
            return 'There is not any element in the stack'
        else:
            return self.list[len(self.list)-1]
    
    # delete
    def delete(self):
        self.list = None

customStack = Stack(4)

print(customStack.isEmpty())

customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)

print(customStack.peek())

customStack.pop()
print(customStack.isFull())


print(customStack.peek())
print(customStack)

# customStack.delete()
# print(customStack)