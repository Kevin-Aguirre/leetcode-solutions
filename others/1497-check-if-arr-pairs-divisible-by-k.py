# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/?envType=daily-question&envId=2024-10-01
# 1497. Check If Array Pairs Are Divisible by k
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        ## RC ##
        ## APPROACH : 2 SUM ##
        ## LOGIC ##
		## 1. Store the remainders in the hashmap and check if the current number has remaining remainder available in the hashset ##
		
        if len(arr) % 2 == 1: return False
        lookup = collections.defaultdict(int)
        count = 0
        for i, num in enumerate(arr):
            key = k - (num % k)
            if key in lookup and lookup[key] >= 1:
                # print(key, num)
                count += 1
                lookup[key] -= 1
            else:
                lookup[(num % k) or k] += 1
        return count == len(arr) // 2