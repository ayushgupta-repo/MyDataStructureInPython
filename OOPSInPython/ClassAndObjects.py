# Example 1: Creating a class and object with class and instance attributes

# class Dog:

#     # class variable: It remains constant for every object
#     attr1 = 'mammal'

#     # Instance variable: Differs for every object
#     def __init__(self, name):
#         self.name = name

# # Driver Code

# # Object Instantiation
# Rodger = Dog('Rodger')
# Tommy = Dog('Tommy')

# # Accessing class attributes
# print('Rodger is a {}'.format(Rodger.attr1))
# print('Tommy is also a {}'.format(Tommy.attr1))

# # Accessing instance variable
# print('My name is {}'.format(Rodger.name))
# print('My name is {}'.format(Tommy.name))

# Example 2: Creating Class and objects with methods

class Dog:

    # class attribute
    attr1 = 'mammal'

    # Instance attribute
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print('My name is {}'.format(self.name))

# Driver Code
# Object Instantiation
Rodger = Dog('Rodger')
Tommy = Dog('Tommy')

# Accessing class methods
Rodger.speak()
Tommy.speak()