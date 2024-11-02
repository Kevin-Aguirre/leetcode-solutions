# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150

from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        
        for s in strs:
            sortedWord = ''.join(sorted(s))
            res[sortedWord].append(s)
        return list(res.values())
