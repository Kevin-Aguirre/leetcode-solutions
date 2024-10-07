# sln: https://leetcode.com/problems/permutations/solutions/5152552/video-simple-backtracking-solution/
# 46. Permutations
# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]

        res = []  
        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)
            res.extend(perms)
            nums.append(n)
        return res