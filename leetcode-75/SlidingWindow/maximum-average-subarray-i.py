"""
https://leetcode.com/problems/maximum-average-subarray-i/description/


Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
 
Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000

 
Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104


"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l = 0 
        r = k - 1

        maxi = float('-inf') 
        windowSum = None
        while (r != len(nums)):
            if (not windowSum):
                windowSum = 0 
                for i in range(l, r + 1):
                    windowSum += nums[i]
            else:
                windowSum += nums[r]

            if ((windowSum / k ) > maxi):
                maxi = windowSum / k
            
            windowSum -= nums[l]
            l += 1
            r += 1
        return maxi