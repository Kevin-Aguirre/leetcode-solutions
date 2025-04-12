# 150. Evaluate Reverse Polish Notation
# Medium
# 04-12-2025
"""You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

 
Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

 
Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

"""
from types import List
class Solution:
    def handleOp(self, n1, n2, op):
        if (op == "+"):
            return n1 + n2
        elif (op == "-"):
            return n1 - n2
        elif (op == "*"):
            return n1 * n2
        else:
            return int(n1 / n2)

    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-*/"
        stack = []

        for tok in tokens:
            if tok not in ops:
                stack.append(int(tok))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                res = self.handleOp(n1, n2, tok)
                print(res)
                stack.append(res)
        return stack[0]


"""
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
["10","6","12","-11","*","/","*","17","+","5","+"]
["10","6","-132","/","*","17","+","5","+"]
["10","-1","*","17","+","5","+"]
["-10","17","+","5","+"]
["7","5","+"]
["12"]
"""