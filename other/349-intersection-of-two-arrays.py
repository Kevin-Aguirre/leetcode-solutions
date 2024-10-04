"""
Approach: HashMap & Sets
Make both lists into sets to deal with duplicates. Iterate through one set, and simply keep track of each element we've seen.
Now as we iterate through the other set, we increment the value of s[n] if we see it again. we return a list of keys where 
the value is 2, that is, we return the key if we've seen it in both nums1 and nums2.

Time Complexity: O(n_1 + n_2) where n_1,n_2 are lengths of nums1 and num2, respectively 
Space Compelxity: O(n_1 + n_2) where n_1,n_2 are lengths of nums1 and num2, respectively 
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = {}
        for n in set(nums1):  
            if n not in s:
                s[n] = 1
        for n in set(nums2): 
            if n in s:
                s[n] += 1

        return [key for key, val in s.items() if val == 2]
