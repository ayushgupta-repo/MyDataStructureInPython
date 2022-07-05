def addTwoLists(list_1, list_2):
    # Write your code here.
    # list_1 = []
    # list_2 = []
    # while first:
    #     list_1.append(first.data)
    #     first = first.next
    # while second:
    #     list_2.append(second.data)
    #     second = second.next
    
    carry = 0
    
    i = len(list_1)-1
    j = len(list_2)-1
    
    while i >= 0 or j >= 0:
        
        if list_1[i] > -1 or list_2[j] > -1:

            if i > -1 and j > -1:
                addition = list_1[i] + list_2[j] + carry
            elif i > -1:
                addition = list_1[i] + carry
            else:
                addition = list_2[j] + carry
        
            if addition > 9:
                carry = 1
                strAddition = str(addition)
                if len(list_1) > len(list_2):
                    list_1[i] = int(strAddition[1])
                else:
                    list_2[j] = int(strAddition[1])
                i -= 1
                j -= 1
            else:
                carry = 0
                if len(list_1) > len(list_2):
                    list_1[i] = addition
                else:
                    list_2[j] = addition
                i -= 1
                j -= 1
        else:
            i -= 1
            j -= 1

    if len(list_1) > len(list_2):
        if carry == 1:
            list_1.insert(0, carry)
        return list_1
    else:
        if carry == 1:
            list_2.insert(0, carry)
        return list_2

if __name__=='__main__':
    print(addTwoLists([1, 1, -1], [9, 9, 9, -1]))