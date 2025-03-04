# Problem 11
# Largest Product in a Grid
# Difficulty rating: 5%
# 03-04-2025

def getProd(arr, n):
    prod = 1
    for i in range(n):
        prod *= arr[i]
    return prod

def getGrid(fname):
    res = []
    with open(fname, 'r') as ifile:
        for line in ifile.readlines():
            strLine = line.strip().split(' ')
            intLine = [int(num) for num in strLine]
            res.append(intLine)
    return res


def getVerticalMax(grid, n):
    vertMax = 0 
    for row in range(len(grid)-n+1):
        for col in range(len(grid[0])):
            print(col)
            currProd = getProd([grid[row][col], grid[row+1][col], grid[row+2][col], grid[row+3][col]], n)
            vertMax = max(currProd, vertMax)

    return vertMax

def getDiagMax2(grid, n):
    diagMax = 0 
    for row in range(len(grid)-n+1):
        for col in range(n-1, len(grid)):
            currProd = getProd([grid[row][col], grid[row+1][col-1], grid[row+2][col-2], grid[row+3][col-3]], n)
            diagMax = max(diagMax, currProd)

    return diagMax

def getHorizontalMax(grid, n):
    horizMax = 0 
    for row in range(len(grid)):
        for col in range(len(grid) - n + 1):
            currProd = getProd(grid[row][col:col+n], n)
            horizMax = max(horizMax, currProd)
    
    return horizMax


def getDiagMax(grid, n):
    diagMax = 0
    for row in range(len(grid)-n+1):
        for col in range(len(grid)-n+1):
            currProd = getProd([grid[row][col], grid[row+1][col+1], grid[row+2][col+2], grid[row+3][col+3]], n)
            diagMax = max(diagMax, currProd)
    return diagMax


def main():
    fileName = "input.txt"
    n = 4
    grid = getGrid(fileName)
    
    vertMax = getVerticalMax(grid, n)
    horizMax = getHorizontalMax(grid, n)
    diagMax = getDiagMax(grid, n)
    diagMax2 = getDiagMax2(grid, n)

    print(max(vertMax, horizMax, diagMax, diagMax2))

main()