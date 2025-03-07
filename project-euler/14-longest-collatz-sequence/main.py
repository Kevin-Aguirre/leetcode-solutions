# Problem 14
# Longest Collatz Sequence
# Difficulty rating: 5%
# 03-07-2025

def getCollSeqLength(n, length = 1):
    if n == 1: return (1, length)
    if n % 2 == 0: 
        return getCollSeqLength(n // 2, length + 1)
    return getCollSeqLength(3 * n + 1, length +1)
    

def main():
    maxStartingNum = None
    maxLength = 0 

    for i in range(1, 1000000):
        if (getCollSeqLength(i)[1] > maxLength):
            maxStartingNum = i
            maxLength = getCollSeqLength(i)[1]
    print(maxStartingNum)


main()

