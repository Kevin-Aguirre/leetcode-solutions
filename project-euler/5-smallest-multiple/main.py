# Problem 5
# Smallest Multiple
# Difficulty rating: 5%
# 03-01-2025

"""
1 * 2 * 3 * 4 * 5 * _6_ * _7_ * _8_ * _9_ * _10_ * n = 2520

get the factors of each number, if the factors is only composesd of trivial factors [n_i, 1], include n_i and move on. if the factors is 
composed of non-trivial factors, [n s.t n!= 1 adnd n!= n_i], then we see if those elements appear in the list, if any elemnts are not in the list 
add it so tha twe could reconstruct the current number. repeat.

5 * 6 * 7 * 8 * 9 * 10 

[3, 2, 2, 5, 7, 2, 3]

Solution: 
* notice how each number past the midpoint (from 6...10) can be found
by multuplying various other numbers. For instance, 

6 = 2 * 3
7 = 7 * 1
8 = 4 * 2
9 = 3 * 3
10 = 5 * 2

So, we can safely disregard the first half numbers since we know the second 
half numbers are either divisble by the second half numbers or prime. 

Now, we have 

6 * 7 * 8 * 9 * 10 = 30240

Which is much bigger than 2520. Why? Well it's because we are reusing factors
like 3 in 2 * 3 = 6, 2 in 2 * 4 = 8 and 2 * 5 = 10.

So, getting rid of the reused factors gets us 

6 * 7 * 8 * 9 * 10 / (2 * 3 * 3) = 2520.0

2 * 3 * 7 * 1 * 2 * 2 * 2

6 * 7 * 8 * 9 * 10 


"""

from collections import Counter

# is nums1 a sublist of nums2
def isSublist(nums1: list[int], nums2: list[int]):
    for n in nums1:
        if nums1.count(n) > nums2.count(n): return False
    return True


def list_difference(lst1, lst2):
    count1 = Counter(lst1)
    count2 = Counter(lst2)
    
    result = []
    for elem in count1:
        result.extend([elem] * (count1[elem] - count2.get(elem, 0)))
    
    return result

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def main():
    nums = [i for i in range(1, 20+1)]
    facts = []
    for n in nums:
        n_facts = prime_factors(n)
        if isSublist(n_facts, facts): continue

        facts.extend(list_difference(n_facts, facts))
    
    prod = 1
    for f in facts:
        prod *= f
    print(prod)

main()