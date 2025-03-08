# Problem 15
# Lattice Paths
# Difficulty rating: 5%
# 03-08-2025

def fact(n): return 1 if n == 0 else n * fact(n-1)

def main():
    n = 20
    print(int(fact(2 * n) / (fact(n) * fact(n))))

main()