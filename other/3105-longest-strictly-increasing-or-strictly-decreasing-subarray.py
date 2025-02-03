# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/?envType=daily-question&envId=2025-02-03

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        """
        [1,4,3,3,2]
        """
        maxLength = 1
        currLength = 1
        for i in range(len(nums) - 1):
            if nums[i+1] > nums[i]: 
                currLength += 1
                maxLength = max(maxLength, currLength)
            else: 
                currLength = 1

        currLength = 1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] > nums[i]: 
                currLength += 1
                maxLength = max(maxLength, currLength)
            else:
                currLength = 1
    
        return maxLength
