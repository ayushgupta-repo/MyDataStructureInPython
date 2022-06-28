# Creating stack and operations based on python list with no size limit

class Stack:
    def __init__(self):
        self.list = [] # no size limit
    
    # for printing
    def __str__(self):
        values = self.list.reverse() # reversing list
        values = [str(x) for x in self.list]

        return '\n'.join(values)

    # isEmpty()
    def isEmpty(self):
        # Checking list is empty
        if self.list == []:
            return True
        else:
            return False

    # push()
    def push(self, value):
        # In case of size limit we need to add checker but not now
        self.list.append(value) # appending value or adding value in list
        return 'The element has been successfully inserted.'

    # pop()
    def pop(self):
        # Checking stack is empty or not
        if self.isEmpty():
            return 'There is not any element in the stack.'
        else:
            return self.list.pop()

    # peek()
    def peek(self):
        # Checking stack is empty or not
        if self.isEmpty():
            return 'There is not any element in the stack.'
        else:
            return self.list[len(self.list)-1]
    
    # delete entire stack
    def delete(self):
        self.list = None

customStack = Stack()

# print(customStack.isEmpty()) # True

# checking push operation
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)

# print(customStack)

# checking peek operation
print(customStack.peek()) # Returns 4 and it will not being deleted

# checking pop operation
print(customStack.pop()) # Returns 4 and it is being deleted

# checking delete entire stack operatoin
customStack.delete()

print(customStack)