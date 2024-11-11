"""
https://leetcode.com/problems/min-cost-climbing-stairs/description/


Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
 
Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

 
Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999


"""
class Solution(object):
    """
    this is not my implementation, it appears to be using a dp approach with 2 variables, which is valid, 
    since we only need to know 2 values at a time 
    """
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        
        cur=0
        dp0=cost[0]
        
        if len(cost) >= 2:
            dp1=cost[1]
        
        for i in range(2, len(cost)):
            cur=cost[i] + min(dp0,dp1)
            dp0=dp1
            dp1=cur
            


        return min(dp0,dp1)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])
