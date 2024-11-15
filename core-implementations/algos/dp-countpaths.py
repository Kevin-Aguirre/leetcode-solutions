
def countPaths(G):
    m = len(G)
    n = len(G[0])
    # Initialize an m x n table T with all entries set to 0
    T = [[0 for _ in range(n)] for _ in range(m)]

    # Setting the first cell to 1 if it isn’t blocked
    if G[0][0] == 0:
        T[0][0] = 1

    # Initializing the first column
    for i in range(1, m):
        if G[i][0] == 0 and T[i - 1][0] == 1:
            T[i][0] = 1

    # Initializing the first row
    for j in range(1, n):
        if G[0][j] == 0 and T[0][j - 1] == 1:
            T[0][j] = 1

    # Filling in the rest of the table
    for i in range(1, m):
        for j in range(1, n):
            if G[i][j] == 0:
                T[i][j] = T[i - 1][j] + T[i][j - 1] + T[i - 1][j - 1]

    # Return the value stored at the bottom-right corner of the table
    return T[m - 1][n - 1]


# Testcase 1: 
# G = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]
     
# Testcase 2
# G = [
#     [0, 0, 1],
#     [0, 1, 0],
#     [0, 0, 0]
# ]

# Testcase 3
G = [[0,0,0,0,0,1,0]]
    
print(countPaths(G))
