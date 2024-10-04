# 1492. The kth Factor of n
# https://leetcode.com/problems/the-kth-factor-of-n/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor_seen = 0 

        for i in range(1, n+1):
            if (n % i == 0):
                factor_seen += 1
            
            if (k == factor_seen): 
                return i 
        return -1