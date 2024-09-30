# https://leetcode.com/problems/max-consecutive-ones/description/
# 485. Max Consecutive Ones

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


