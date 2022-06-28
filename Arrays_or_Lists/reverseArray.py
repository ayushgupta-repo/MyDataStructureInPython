# Iterative way
def iterRev(arr):
    revNum = []
    for i in range(len(arr)):
        revNum.append(arr.pop())

    return revNum

# Recursive way
def recRev(sample, start, end):
    if start >= end:
        return
    sample[start], sample[end] = sample[end], sample[start]
    recRev(sample, start+1, end-1)

if __name__ == '__main__':
    samples = [[3,2,1,4], ['A','B','C','D']]

    for sample in samples:
        print('Simple Array:', sample)
        result = iterRev(sample)

        print('Iterative approach:')
        print('Reversed Array:', result)

        recRev(sample, 0, len(sample))
        print('Recursive approach:')
        print('Reversed Array:', sample)