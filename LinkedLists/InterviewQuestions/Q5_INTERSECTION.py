# Question - 5: Intersection between linked list not on the basis of value but on the basis of reference

from linkedlist import LinkedList, Node

# intersection method
def intersection(llA, llB):
    # Checking if their tails point to the same node or not
    if llA.tail is not llB.tail:
        return False
    # Otherwise

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)

    longerNode = longer.head
    shorterNode = shorter.head

    # traversing longer node to start from same point
    for i in range(diff):
        longerNode = longerNode.next

    # Do traversing and finding the interesction point
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode

# creating method to create intersection point
def addSameNode(llA, llB, value):
    tempNode = Node(value)
    # connecting both linkedlists tail and tail reference to this tempNode
    llA.tail.next = tempNode
    llA.tail = tempNode

    llB.tail.next = tempNode
    llB.tail = tempNode

llA = LinkedList()
llA.generate(3,0,10)

llB = LinkedList()
llB.generate(4,0,10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print(llA)
print(llB)

print(intersection(llA, llB))