# Question-1: Remove Duplicates from linked list

from linkedlist import LinkedList

# With using temporary buffer (visited set) as it creates Space Complexity: O(n) and Time Complexity: O(n)
def removeDuplicates(ll):
    # Checking existence of ll
    if ll.head is None:
        return
    # Otherwise
    else:
        curNode = ll.head
        visited = set([curNode.value])

        while curNode.next:
            # Checking repetition logic
            if curNode.next.value in visited:

                # connecting next reference of current node to the next reference of the next node of curNode
                curNode.next = curNode.next.next
            
            # Adding nonrepeated value to visited
            else:
                visited.add(curNode.next.value)
                curNode = curNode.next

        return ll

# customLL = LinkedList()

# customLL.generate(10, 0, 99)
# print(customLL)

# removeDuplicates(customLL)
# print(customLL)

# Without using temporary buffer (visited set) as it creates Space Complexity: O(1) but Time Complexity: O(n^2)
def removeDuplicates1(ll):
    # Checking existence of ll
    if ll.head is None:
        return
    # Otherwise
    else:
        curNode = ll.head

        while curNode:
            runner = curNode # setting runner node as it will traverse and compare to the curNode

            while runner.next:

                if runner.next.value == curNode.value:
                    runner.next = runner.next.next # connecting runner next to the next of the repeatedNode
                
                else:  
                    runner = runner.next

            curNode = curNode.next

        return ll.head

customLL = LinkedList()

customLL.generate(10, 0, 99)
print(customLL)

print(removeDuplicates1(customLL))
print(customLL)