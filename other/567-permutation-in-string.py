# https://leetcode.com/problems/permutation-in-string/?envType=daily-question&envId=2024-10-05
# 567. Permutation in String

"""
Approach 1: HashMap & Fixed Sliding Window 
In order for s1 to have a permutation s2, either the two strings must be the same size or s1 must be smaller. 

Now, create frequency maps of the first k elements from s1 and s2, where k = len(s1)
Then we use a fixed sliding window, updating the frequencies of the elements at l + 1 and r + 1, 
to account for this the loop ends when r = len(s2) - 1, i.e. r doesn't arrive at last element of s2, 
so we will be able to read the last element without index error. if at any point the two maps are the 
same, return true. 

Time Complexity: O(n1 + n2)
Space Complexity: O(n1 + n2)
"""

from collections import defaultdict 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s2) < len(s1)):
            return False
        
        s1map, s2map = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            s1map[s1[i]] += 1
            s2map[s2[i]] += 1
            
        l = 0 
        r = len(s1) - 1
        while (r < len(s2)-1):
            if (s1map == s2map): return True
            
            s2map[s2[l]] -= 1
            if s2map[s2[l]] == 0:
                del s2map[s2[l]]
            
            if s2[r+1] not in s2map:
                s2map[s2[r+1]] = 1
            else:
                s2map[s2[r+1]] += 1

            l += 1
            r += 1

        return s1map == s2map

