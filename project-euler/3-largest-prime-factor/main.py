# Problem 3
# Largest Prime Factor
# Difficulty rating: 5%
# 02-28-2025

"""
continously divide the square root for i ... sqrt

"""

import math 

def isPrime(n): 
    for i in range(2, (n // 2) + 1):
        if n % i == 0: 
            return False
    return True 

def main():
    
    n = 600851475143
    sq_n = math.ceil(math.sqrt(n))

    prime_factors = []


    while (n > sq_n):
        for i in range(2, sq_n):
            if n % i == 0: 
                prime_factors.append(i)
                if isPrime(n // i):
                    prime_factors.append(n // i)
                n //= i 
                break 
    
    print(max(prime_factors))

main()
