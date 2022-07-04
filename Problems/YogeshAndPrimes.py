def findP(A, B, K):
    P = A

    while P <= B:
        if K > 0:
            flag = False
            if P > 1:
                for i in range(2, int(P/2)+1):
                    if (P % i) == 0:
                        flag = True
                        break
            
            if P == 1:
                flag = True

            if flag:
                P += 1
            else:
                P += 1
                K -= 1
        else:
            break

    if P-1 == B and A!=B:
        return -1

    return P-1


if __name__ == '__main__':
    print(findP(5, 5, 1))
