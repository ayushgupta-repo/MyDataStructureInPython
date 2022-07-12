def xorQuery(queries):
    # Write your code here.
    operated_arr = []
    for each_query in queries:
        if each_query[0] == 1:
            operated_arr.append(each_query[1])
        elif each_query[0] == 2:
            for i in range(len(operated_arr)):
                operated_arr[i] = operated_arr[i] ^ each_query[1]
    
    return operated_arr

if __name__=='__main__':
    T = int(input())
    queries = []

    for _ in range(T):
        Q = int(input())

        # queries = [[]] * Q

        for i in range(Q):
            queries.append(list(map(int, input().split())))
    
        print(xorQuery(queries))