# Problem 7
# 10 001st Prime
# Difficulty rating: 5%
# 03-02-2025

def isPrime(n): 
    for i in range(2, (n // 2) + 1):
        if n % i == 0: 
            return False
    return True 


def main():
    cnt = 0 
    i = 1
    while cnt < 10001:
        i += 1
        if isPrime(i):
            cnt += 1
    print(i) 

main()
