class Solution:
    # stack 
    # def minAddToMakeValid(self, s: str) -> int:
    #     stack = []

    #     for c in s:
    #         if stack:
    #             if stack[-1] == '(' and c == ')':
    #                 stack.pop()
    #             else:
    #                 stack.append(c)
    #         else:
    #             stack.append(c)

    #     return len(stack)
    
    def minAddToMakeValid(self, s: str) -> int:
        open_c = close_c = 0
        for c in s:
            if c == '(':
                open_c += 1
            elif c == ')' and open_c > 0:
                open_c -= 1
            else:
                close_c += 1
        return open_c + close_c