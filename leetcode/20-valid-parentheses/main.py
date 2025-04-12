# 20. Valid Parentheses
# Easy
# 04-12-2025
"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

 
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([])"
Output: true

 
Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {")":"(", "]":"[", "}":"{"}
        arr = []

        for c in s:
            if c in m.values():
                arr.append(c)
            else:
                if not arr or arr[-1] != m[c]:
                    return False
                arr.pop()
        return not arr