# Question-3: Stack of plates
# If stack reaches it's capacity or threshold than create new substack
# Also implement pop_at(sub-stacknumber) to pop from specific substack

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [] # empty stack to store sub-stacks

    def __str__(self):
        return str(self.stacks)
    
    def push(self, item):
        # Checking that the length of stack is greater than 0 and also the length of last sub-stack reached to it's capacity or not to create new sub-stack
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item) # append item at last stack
        else:
            self.stacks.append([item]) # else create new sub-stack
    
    def pop(self):
        # Checking if length of stack is zero and last sub-stack element is present or not
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        # Checking if stacks empty or not
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop() # removing element from last sub-stack
    
    def pop_at(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return False

customStack = Stack(2)

customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)

print(customStack)

print(customStack.pop()) # returns 4 and will be deleted
print(customStack)

print(customStack.pop_at(0)) # returrns 2 and will be deleted
print(customStack)