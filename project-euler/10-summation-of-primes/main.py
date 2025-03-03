# Problem 10
# Summation of Primes
# Difficulty rating: 5%
# 03-03-2025

import math

def isPrime(n): 
    if (n < 2): return False
    if (n == 2): return True

    for i in range(2, math.ceil(math.sqrt(n)) + 1, 1):
        if n % i == 0: 
            return False
    return True 


def main():
    p = 3
    total = 2
    while (p < 2000000):
        if (isPrime(p)):
            print(p)
            total += p

        p += 2
    print(total)
main()