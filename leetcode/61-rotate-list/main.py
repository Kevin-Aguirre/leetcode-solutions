# 61. Rotate List
# Medium
# 04-16-2025
"""Given the head of a linked list, rotate the list to the right by k places.
 
Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]

 
Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head):
        if not head: return 0
        return 1 + self.getLength(head.next)

    def rotateRight(self, head, k):
        n = self.getLength(head)
        if not head: return None
        if k == 0: return head
        if k % n == 0: return head
        
        k = k % n

        curr = head
        for _ in range(n - k - 1):
            curr = curr.next
        
        newHead = curr.next
        curr.next = None
        newCurr = newHead
        while (newCurr.next):
            newCurr = newCurr.next
        
        newCurr.next = head
        return newHead