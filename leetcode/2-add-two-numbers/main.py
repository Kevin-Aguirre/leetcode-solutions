# 2. Add Two Numbers
# Medium
# 05-06-2025
"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 
Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""
from types import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = l1, l2

        dummy = ListNode()
        res = dummy 
        carry = 0
        while (c1 and c2):
            currSum = c1.val + c2.val 
            if carry: currSum += carry 
            carry = currSum // 10 
            leftover = currSum % 10 
            res.next = ListNode(leftover)
             
            res = res.next
            c1 = c1.next
            c2 = c2.next
        
        c3 = c1 if c1 else c2 
        while (c3):
            currSum = c3.val + carry
            carry = currSum // 10 
            leftover = currSum % 10 
            res.next = ListNode(leftover)
            res = res.next
            c3 = c3.next
        
        if carry: res.next = ListNode(carry)

        return dummy.next
