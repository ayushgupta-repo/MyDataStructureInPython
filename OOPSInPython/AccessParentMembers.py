# Python example to show that base
# class members can be accessed in
# derived class using base class name

class Base(object):

    # Constructor
    def __init__(self, x):
        self.x = x

class Derived(Base):

    # Constructor
    def __init__(self, x, y):
        Base.x = x
        self.y = y

    def printXY(self):

        # print(self.x, self.y) will also work
        print(Base.x, self.y)

# Driver Code
d = Derived(10, 20)
d.printXY()