# https://leetcode.com/problems/max-consecutive-ones/description/
# 485. Max Consecutive Ones

"""
Approach 1: 
Trivial approach, count the number of ones as they come while iterating through nums. When anything but a 1 is encountered, 
update the max number of consecutive ones we've encountered.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
            
        maxOnes, curr = 0, 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                curr = 0
            maxOnes = max(curr, maxOnes)
            
        return maxOnes


