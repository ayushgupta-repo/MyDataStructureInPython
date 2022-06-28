# Initializing Tree
# Method-1: Using dict() class to create object and perform operations on that.
# Method-2: By creating dictName = {}

myDict = {}

myDict = {'name': 'Edy', 'age': 26}

print(myDict) # {'name': 'Edy', 'age': 26}

# updating value by using key
# myDict['age'] = 25

# print(myDict) # {'name': 'Edy', 'age': 25}

# adding new key-value pair to pre-existed dictionary
myDict['address'] = 'London'
print(myDict) # {'name': 'Edy', 'age': 26, 'address': 'London'}

# traversing through a dictionary

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

# traverseDict(myDict) # prints key with its value

# searching for an element in a dictionary
def searchDict(dict, value):
    for key in dict:
        if value == dict[key]:
            return key, value
    return 'The value does not exist.'

# print(searchDict(myDict, 'London')) # Returns key, value pair
# print(searchDict(myDict, 'India')) # Returns The value does not exist.

# deleting an element from a dictionary
# Method-1: Using pop() method

# print(myDict.pop('name')) # by providing key it returns the value and it will get deleted
# print(myDict)

# Method-2: Using popitem() method
# print(myDict.popitem()) # It returns random key-value pair and it will get deleted
# print(myDict)

# Method-3: Using clear() method
# It deletes entire dictionary
# myDict.clear() # clear complete dictionary
# print(myDict)

# Method-4: Using del method
# del myDict['age'] # it deletes the key-value pair of which key is provided
# print(myDict)

# Dictionary Methods:
# 1. clear() -> deletes entire dictionary
# 2. copy() -> returns a shallow copy of a dictionary
# 3. fromkeys() -> creates and returns key-value pair as passed in which first parameter will be keys list and second is the value assigned to those keys

# newDict1 = {}.fromkeys([1,2,3], 0)
# print(newDict1) # {1:0, 2:0, 3:0}

# newDict2 = {}.fromkeys([1,2,3])
# print(newDict2) # {1: None, 2: None, 3: None}

# 4. get() -> Returns value of specified key
# print(myDict.get('name'))

# 5. items() -> Returns dictionary key-value pair in tuple pair
print(myDict.items()) # dict_items([('name', 'Edy'), ('age', 26), ('address', 'London')])

# 6. keys() -> Returns list of all keys in dictionary
print(myDict.keys()) # dict_keys(['name', 'age', 'address'])

# 7. popitem() -> Returns key-value pair and it gets deleted

# 8. setdefault() -> Sets new key-value pair with default value and it default value as second parameter is not passed then it will be set to None
print(myDict.setdefault('name', 'added')) # Since name as key and it's value is already existed so added will not get assigend to that key

print(myDict.setdefault('name1', 'added')) # Since name1 as key and it's value not existed so it will be added with default value
print(myDict)

# 9. pop() -> Returns value and it will be deleted

# 10. values() -> Returns list of values in dictionary
print(myDict.values()) # dict_values(['Edy', 26, 'London', 'added'])

# 11. update() -> It updates the pre-existing key-value pair