# 242. Valid Anagram
# Easy
# 04-12-2025
"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        h1, h2 = {}, {}

        for i in s: 
            if h1.get(i):
                h1[i] += 1
            else:
                h1[i] = 1
        
        for j in t:
            if h2.get(j):
                h2[j] += 1
            else:
                h2[j] = 1
        
        return h1 == h2
        