# Question - 4: Traverse the numbers in the list and merge those numbers to create one number
                # Then reverse the numbers and do sum and then again return the sumlist (linkedlist)

from linkedlist import LinkedList

# creating number
def createNumber(ll):
    # Do traversal and return the number
    number = ''

    node = ll.head

    while node:
        number += str(node.value)
        node = node.next
    
    return int(number)

# reversing number
def reverseNumber(num):
    nums = []

    while num >= 10:
        nums.append(str(num%10))
        num = num // 10
    
    nums.append(str(num))

    return int(''.join(nums))

def main():
    list1 = LinkedList()
    list2 = LinkedList()

    list1.generate(4, 1, 9)
    list2.generate(4, 1, 9)

    print('Linked List 1:', list1)
    print('Linked List 2:', list2)

    # extracting numbers from linked list
    num1 = createNumber(list1)
    num2 = createNumber(list2)

    print('Extracted number 1:', num1)
    print('Extracted number 2:', num2)

    # reversing the extracted numbers
    revNum1 = reverseNumber(num1)
    revNum2 = reverseNumber(num2)

    print('Reverse number 1:', revNum1)
    print('Reverse number 2:', revNum2)

    sum = revNum1 + revNum2

    # Note: You need to reverse sum in case of add functionality in your linked list is insertion from the beginning but in my case it is insertion from the last

    print('Sum:', sum)

    sumList = LinkedList()

    while sum >= 10:
        sumList.add(sum%10)

        sum = sum // 10

    sumList.add(sum)


    print('Sum list:', sumList)

main()