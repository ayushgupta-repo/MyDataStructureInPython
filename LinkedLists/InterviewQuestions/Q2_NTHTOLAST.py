# Question-2: Find Nth from Last in the SinglyLinkedList

from linkedlist import LinkedList

# My Approach:
# 1. Getting length of ll (given linked list)
# 2. Getting uptoTraverse (length of ll - N (location of element to find from last))
# 3. Do traversal and reach to that node and return it
def findElement(ll, N):
    # Checking existence of ll
    if ll.head is None:
        return
    
    # Otherwise
    else:
        # Getting length of ll
        length = len(ll)

        uptoTraverse = length-N

        # Do traversal and print the output

        curNode = ll.head
        index = 0

        while index < uptoTraverse:
            curNode = curNode.next
            index += 1

        return curNode.value

# customLL = LinkedList()

# customLL.generate(10, 0, 99)
# print(customLL)

# print(findElement(customLL, 5))

# Another Approach:
# 1. Setting pointer1 and pointer2 to head
# 2. Make difference between pointer1 and pointer2 to the N gap
# 3. Move both pointers until pointer2 reaches the lastNode and the finding element will be pointed by pointer1

def nthToLast(ll, n):
    # Setting pointers
    pointer1 = ll.head
    pointer2 = ll.head

    # Making difference between pointers
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    
    # Moving both pointers until pointer2 reaches to lastNode
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1

customLL = LinkedList()

customLL.generate(10, 0, 99)
print(customLL)

print(nthToLast(customLL, 4))