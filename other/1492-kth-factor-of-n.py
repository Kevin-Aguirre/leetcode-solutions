# 1492. The kth Factor of n
# https://leetcode.com/problems/the-kth-factor-of-n/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
class Solution:
    """
    Approach 1: Intuitive Solution
    Simply iterate over integers leading up to n and count how many divide k. Once our count is equal to k 
    return that current factor.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def kthFactor(self, n: int, k: int) -> int:
        factor_seen = 0 

        for i in range(1, n+1):
            if (n % i == 0):
                factor_seen += 1
            
            if (k == factor_seen): 
                return i 
        return -1