"""
https://leetcode.com/problems/generate-parentheses/description/


Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]

 
Constraints:

1 <= n <= 8


"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        