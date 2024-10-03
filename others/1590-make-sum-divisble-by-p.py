# https://leetcode.com/problems/make-sum-divisible-by-p/solutions/854895/how-to-approach-this-kind-of-problem-mind-map/?envType=daily-question&envId=2024-10-03
# 1590. Make Sum Divisble by P
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums)%p==0:
            return 0
        target = sum(nums) % p
        dic,n = {0:-1},len(nums)
        cur,ret = 0,n
        for i,num in enumerate(nums):
            cur = (cur+num)%p
            if dic.get((cur-target)%p) is not None:
                ret = min(ret,i-dic.get((cur-target)%p))
            dic[cur] = i
        return ret if ret < n else -1