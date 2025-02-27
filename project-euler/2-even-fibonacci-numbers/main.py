# Problem 2
# Even Fibonacci Numbers
# Difficulty rating: 5%
# 02-27-2025


def main():

    n1, n2 = 1, 2
    res = 2

    while n2 < 4000000:
        nxt = n1 + n2 
        if (nxt % 2 == 0):
            res += nxt
        n1 = n2   # 2,000,000
        n2 = nxt # 3,000,000
    print(res)

main()