# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/solutions/6017268/easiest-solution-beats-100-c-java-python3-javascript/
# 2275. Largest Combination With Bitwise AND Greater Than Zero


class Solution:
    def largestCombination(self, nums: List[int]) -> int:
        ans = 0
        for _ in range(32):
            a = 0
            for i in range(len(nums)):
                if nums[i] & 1: a+=1
                nums[i] >>=1
            ans= max(ans, a)
        return ans
