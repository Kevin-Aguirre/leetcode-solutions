# 125. Valid Palindrome
# Easy
# 04-12-2025
"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
 
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 
Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""
class Solution:
    def isValidChar(self, c: str) -> bool:
        return (ord('a') <= ord(c.lower()) <= ord('z')) or (ord('0') <= ord(c.lower()) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        start = 0 
        end = len(s) - 1

        while start <= end:


            if (not self.isValidChar(s[start])):
                start += 1
            elif (not self.isValidChar(s[end])):
                end -= 1
            elif (s[start].lower() == s[end].lower()):
                start += 1
                end -=1 
            else:
                return False

        return True
