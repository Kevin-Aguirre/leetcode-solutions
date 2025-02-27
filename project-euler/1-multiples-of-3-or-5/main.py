# Problem 1
# Multiples of 3 or 5
# Difficulty rating: 5%
# 02-27-2025

def main():
    res = 0 
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            res += i

    print(res)

main()