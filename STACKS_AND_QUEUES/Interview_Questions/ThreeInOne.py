# Question-1 : Three In One
# Describe how you could use a single python list to implement three stacks.

# Use a single list to implement three stacks.
class MultiStack:
    def __init__(self, stacksize):
        self.numberStacks = 3 # fixed number of stacks as per the question it is 3
        self.custList = [0] * (stacksize * self.numberStacks)
        self.sizes = [0] * self.numberStacks # size of each stack
        self.stacksize = stacksize # max size of each stack
    
    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False

    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False
    
    # helper method that returns the index of top of the stack
    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1
    
    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return 'The stack is full'
        else:
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] = item
    
    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return 'The stack is empty'
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value
    
    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return 'The stack is empty'
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            return value

customStack = MultiStack(6)
print(customStack.isFull(0)) # False
print(customStack.isEmpty(1)) # True

customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)

print(customStack.peek(1)) # The stack is empty
print(customStack.peek(0)) # 2
print(customStack.pop(0)) # 2 and it will be deleted
print(customStack.peek(0)) # 1
