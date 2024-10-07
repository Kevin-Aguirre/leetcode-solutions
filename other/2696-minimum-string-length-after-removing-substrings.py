# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
# Minimum String Length After Removing Substrings
# Note, this exact question was asked by IBM in an Online Assessment
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for char in s:
            if stack:
                if stack[-1] == 'A' and char == 'B':  
                    stack.pop()  
                elif stack[-1] == 'C' and char == 'D':  
                    stack.pop()  
                else:
                    stack.append(char) 
            else:
                stack.append(char)  
        

        return len(stack)