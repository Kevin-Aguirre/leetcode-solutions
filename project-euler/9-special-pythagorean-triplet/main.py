# Problem 9
# Special Pythagorean Triplet
# Difficulty rating: 5%
# 03-02-2025

# could be optimized by removing loop for c, an djust having loops for a and b, and computing c, then checking if it meets requirements 

def main():
    for c in range(1000):
        for b in range(c): # b is upper bounded by c (b < c)
            for a in range(b): # a is upper bounded by b (a < b and thus a < b < c)
                if (a + b + c == 1000) and (a ** 2 + b ** 2 == c ** 2):
                    print(a * b * c)
                    break
main()