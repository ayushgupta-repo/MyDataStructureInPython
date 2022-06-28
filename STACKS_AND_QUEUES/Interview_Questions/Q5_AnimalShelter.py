# Question-5: Animal Shelter
# Implement enqueue, dequeuAny, dequeueCat and dequeueDog

class AnimalShelter():
    def __init__(self):
        # creating two lists
        self.cats = []
        self.dogs = []
    
    def enqueue(self, item, type):
        if type == 'Cat':
            self.cats.append(item)
        else:
            self.dogs.append(item)
    
    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop(0)
            return cat
    
    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop(0)
            return dog
    
    def dequeueAny(self):
        # NOTE: First priority will be Cat and second priority will be Dog
        if len(self.cats) == 0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result

customQueue = AnimalShelter()

customQueue.enqueue('Cat1', 'Cat')
customQueue.enqueue('Cat2', 'Cat')
customQueue.enqueue('Dog1', 'Dog')
customQueue.enqueue('Dog2', 'Dog')

print(customQueue.dequeueCat()) # Cat1
print(customQueue.dequeueCat()) # Cat2

# print(customQueue.dequeueDog()) # Dog1
# print(customQueue.dequeueDog()) # Dog2
print(customQueue.dequeueAny()) 