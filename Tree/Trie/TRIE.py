# Creating Trie Tree
# It is basically a data-structure that organizes information hierarichaly

class TrieNode:
    def __init__(self):
        self.children = {} # Using dictionary to manage relation of it's child
        self.endOfString = False # To store end of string (If ends then it will be true)

class Trie:
    def __init__(self):
        self.root = TrieNode() # Initializing Trie Tree

    def insertString(self, word):
        currentNode = self.root

        # traversing each word
        for i in word:
            ch = i
            node = currentNode.children.get(ch) # checking if ch exists

            # If it does not exist
            if node == None:
                node = TrieNode() # creating node
                currentNode.children.update({ch:node}) # updating children of currentNode
            currentNode = node # updating currentNode

        # setting endOfString to True after insertion
        currentNode.endOfString = True
        print('Successfully Inserted')

    # search for a string in Trie
    def searchString(self, word):
        currentNode = self.root

        # traversing each characters
        for i in word:
            node = currentNode.children.get(i)

            # CASE-1 (String does not exist in Trie)
            if node == None:
                return False
            
            # updating current node
            currentNode = node

        # CASE-2 (String exist in Trie)
        if currentNode.endOfString == True:
            return True
            
        # CASE-3 (String is a prefix of another string, but it does not exist in Trie)
        else:
            return False

# deleting node
def deleteString(root, word, index):
    ch = word[index] # setting ch to the index passed character (initially it is zero)
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False # Further used in CASE-4

    # CASE-1 (Some other prefix of string is same as the one that we want to delete.)
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    
    # CASE-2 (The string is a prefix of other string.)
    if index == len(word)-1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            # delete the node
            root.children.pop(ch)
            return True

    # CASE-3 (Other string is a prefix of this string.)
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index+1) # Based on above return values it is get modified
    # CASE-4 (Not any node depends on this string.)
    if canThisNodeBeDeleted == True:
        # delete the node
        root.children.pop(ch)
        return True
    else:
        return False

        

        

newTrie = Trie()

newTrie.insertString('App')
newTrie.insertString('Apps')

# print(newTrie.searchString('App'))
# print(newTrie.searchString('Ap'))

deleteString(newTrie.root, 'Apps', 0)
print(newTrie.searchString('App'))
# print(deleteString(newTrie, 'newApp', 0))