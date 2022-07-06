# A Python program to demonstrate inheritance 
  
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is 
# equivalent to "class Person(object)"

# class Person(object):

#     # Constructor
#     def __init__(self, name):
#         self.name = name
    
#     # To get name
#     def getName(self):
#         return self.name
    
#     # To check if this person is employee
#     def isEmployee(self):
#         return False

# # Inherited or Sub class (Note Person in bracket)
# class Employee(Person):

#     # Here we return true
#     def isEmployee(self):
#         return True

# # Driver Code
# emp = Person('Geek1') # An Object of Person
# print(emp.getName(), emp.isEmployee())

# emp = Employee('Geek2') # An Object of Employee
# print(emp.getName(), emp.isEmployee())

# Python example to check if a class is
# subclass of another

class Base(object):
    pass # Empty class

class Derived(Base):
    pass # Empty class

# Driver Code
print(issubclass(Derived, Base))
print(issubclass(Base, Derived))

d = Derived()
b = Base()

# b is not an instance of Derived
print(isinstance(b, Derived))
print(isinstance(d, Base))