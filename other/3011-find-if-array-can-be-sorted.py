# 3011. Find if Array Can Be Sorted
# https://leetcode.com/problems/find-if-array-can-be-sorted/description/?envType=daily-question&envId=2024-11-06

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        pmax = cmin = cmax = pcnt = 0

        for v in nums:
            ccnt = v.bit_count()
            if pcnt == ccnt:
                cmin = min(cmin, v)
                cmax = max(cmax, v)
            elif cmin < pmax:
                return False
            else:
                pmax = cmax
                cmin = cmax = v
                pcnt = ccnt
        return cmin >= pmax
