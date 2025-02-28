# Problem 4
# Largest Palindrome Product
# Difficulty rating: 5%
# 02-28-2025

def isPalindrome(n):
    reverse = 0

    temp = n
    while temp != 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10

    return (reverse == n)

def main():
    pal = []
    for i in range(1000):
        for j in range(1000):
            if (isPalindrome(i * j)):
                pal.append(i * j)

    print(max(pal))


main()