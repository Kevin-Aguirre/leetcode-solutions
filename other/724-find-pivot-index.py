# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75
# 724. Find Pivot Index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)

        for i, e, in enumerate(nums):
            r -= e
            if l == r: return i
            l += e
        return -1 
