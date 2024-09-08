#    Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # step 1: count teh number of nodes 
        count = 0 
        curr = head 
        while (curr):
            count += 1
            curr = curr.next 
        
        # step 2: calculate the size of each part and the number of extra nodes 
        part_size = count // k 
        extra_nodes = count % k

        #step 3, split list into k parts 
        res = [] 
        curr = head

        for i in range(k):
            curr_part_head = curr 
            for j in range(part_size - 1 + (i < extra_nodes)):
                if curr: 
                    curr = curr.next 
            if curr:
                next_node = curr.next 
                curr.next = None 
                curr = next_node 
            res.append(curr_part_head)
        
        return res