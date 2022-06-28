# Question-3: Write code to partition a linked list around a value x
                # such that nodes less than x come before all nodes greater than or equal to x.

from linkedlist import LinkedList

def partition(ll, x):
    curNode = ll.head # seting curNode to head
    ll.tail = ll.head # seting tail to curNode

    while curNode:
        nextNode = curNode.next # refering next of curNode
        curNode.next = None # seting curNode next reference to null
        
        # comparison logic
        if curNode.value < x:
            curNode.next = ll.head # set next of curNode to the head as set previous
            ll.head = curNode # seting head to this curNode

        else:
            ll.tail.next = curNode # if value is greater than or equal to x then add it to last by connecting tail next reference to curNode
            ll.tail = curNode # connecting tail and curNode
        
        curNode = nextNode # traversing

    # Below is done to set tail next reference to none if any node is setted to last in that scenario
    if ll.tail.next is not None:
        ll.tail.next = None

customLL = LinkedList()

customLL.generate(10, 0, 99)
print(customLL)

partition(customLL, 30)
print(customLL)