# Simple Tree
from tkinter.tix import Tree


class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = ' ' * level + str(self.data) + '\n'
        
        # looping through to get child nodes
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)

# Creating restaurant drinks menu

# Creating nodes
tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])

# adding/creating childs
tree.addChild(cold)
tree.addChild(hot)

cold.addChild(cola)
cold.addChild(fanta)

hot.addChild(tea)
hot.addChild(coffee)

print(tree)