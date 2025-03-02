# Problem 6
# Sum Square Difference
# Difficulty rating: 5%
# 03-01-2025

def main(): 
    n = 100
    sum_squares = (n * (n + 1) * (2 * n + 1)) // 6
    square_sums = ((n * (n + 1)) // 2) ** 2
    print(square_sums - sum_squares)
main()