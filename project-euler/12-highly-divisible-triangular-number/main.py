# Problem 12
# Highly Divisible Triangular Number
# Difficulty rating: 5%
# 03-05-2025

import math 
def getFactors(n):
    factors = set()
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if (n % i == 0):
            factors.add(i)
            factors.add(n // i)

    return factors

def main():
    triang_num = 1 
    adder = 2

    facs = getFactors(triang_num)
    while (len(facs) <= 500):

        triang_num += adder
        adder += 1
        facs = getFactors(triang_num)

    print(triang_num)
main()