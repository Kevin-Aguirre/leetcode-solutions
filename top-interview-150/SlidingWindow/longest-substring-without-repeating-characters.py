"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
 
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 
Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


"""
class Solution:
    """
    Approach: Intialize left pointer as 0, hold a character set, have a result variable. 
    Iterate through the string, using it as a right pointer. 
    
    if we encounter that the char 
    of s at index right is in the character set, we have to shorten the window from the left 
    side until that new character we encountered is removed from the set, as we do this we are 
    incrementing left pointer. 

    whether or not we found an element that occured in the set, we add the new character to the set,
    update the maximum length using the values of left and right, and adding 1 because indexing 
    and inclusiveness and math. 
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        charSet = set() 
        l = 0

        for r in range(len(s)):
            while (s[r] in charSet):
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, (r - l) + 1)
            
        
        return res 
