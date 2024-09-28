# 263. Ugly Number
# https://leetcode.com/problems/ugly-number/?envType=problem-list-v2&envId=math

class Solution:
    def isUgly(self, n: int) -> bool:
        if (n <= 0):
            return False
        
        if (1 <= n <= 2):
            return True 

        allowedFacs = [2, 3, 5]
        for fac in allowedFacs:
            if (n % fac) == 0:
                return self.isUgly(n // fac)
        return False