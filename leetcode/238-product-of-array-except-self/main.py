# 238. Product of Array Except Self
# Medium
# 04-12-2025
"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
 
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 
Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = 1 
        prefixArr = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            prefixArr[i] = prefix 

        postfix = 1
        postfixArr = [1] * len(nums)
        for j in range(len(nums) - 2, -1, -1):
            postfix *= nums[j + 1]
            postfixArr[j] = postfix

        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefixArr[i] * postfixArr[i]

        return res