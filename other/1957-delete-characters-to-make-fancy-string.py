# https://leetcode.com/problems/delete-characters-to-make-fancy-string/
# 1957. Delete Characters to Make Fancy String

class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for c in s: 
            if len(stack) < 2: 
                stack.append(c)
            else:
                if not((stack[-1] == stack[-2]) and (c == stack[-1])):
                    stack.append(c)

        return ''.join(stack)

