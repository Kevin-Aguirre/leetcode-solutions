# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int: 
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    def climbStairs(self, n: int) -> int: 
        d1, d2 = 1, 1

        for _ in range(2, n+1):
            temp = d1 + d2
            d1 = d2 
            d2 = temp

        return d2

