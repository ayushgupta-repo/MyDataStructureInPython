# def addTwo(l1, l2):
#     list_1 = []
#     list_2 = []
#     # while l1:
#     #     list_1.append(l1.val)
#     #     l1 = l1.next

#     # while l2:
#     #     list_2.append(l2.val)
#     #     l2 = l2.next

#     for i in l1:
#         list_1.append(i)

#     for j in l2:
#         list_2.append(j)

#     list_1.reverse()
#     list_2.reverse()

#     sum = []
#     i = len(list_1)-1
#     j = len(list_2)-1
#     carry = 0

#     while i >= 0 or j >= 0:
#         if j < 0:
#             addition = list_1[i] + carry
#         else:
#             addition = list_1[i] + list_2[j] + carry

#         if i != 0:
#             sum.append(addition%10)
#         else:
#             num_1 = addition%10
#             num_2 = addition//10

#             sum.append(num_1)
#             sum.append(num_2)

#         if addition > 9:
#             carry = 1
#         else:
#             carry = 0

#         i -= 1
#         j -= 1

#     return sum


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertNode(self, nodeValue):
        newNode = ListNode(nodeValue)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode


class Solution:
    def addTwoNumbers(self, l1, l2):

        list_1 = [node.val for node in ll1]
        list_2 = [node.val for node in ll2]

        list_1.reverse()
        list_2.reverse()

        sum = []
        i = len(list_1)-1
        j = len(list_2)-1
        carry = 0

        while i >= -1 or j >= 0:
            if j < 0:
                addition = list_1[i] + carry
            else:
                addition = list_1[i] + list_2[j] + carry

            if i > -1:
                sum.append(addition % 10)
            else:
                num_1 = addition % 10
                num_2 = addition//10

                sum.append(num_1)
                sum.append(num_2)

            if addition > 9:
                carry = 1
            else:
                carry = 0

            i -= 1
            j -= 1

        # creating linkedlist object
        ll = LinkedList()

        for i in sum:
            ll.insertNode(i)

        return ll, sum


sol = Solution()

ll1 = LinkedList()
ll1.insertNode(9)
ll1.insertNode(9)
ll1.insertNode(9)
ll1.insertNode(9)
ll1.insertNode(9)
ll1.insertNode(9)

ll2 = LinkedList()
ll2.insertNode(9)
ll2.insertNode(9)
ll2.insertNode(9)
ll2.insertNode(9)

print([node.val for node in ll1])
print([node.val for node in ll2])

sumll, sum = sol.addTwoNumbers(ll1, ll2)

print([node.val for node in sumll])

print(sum)
