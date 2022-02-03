from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        seen = []
        while cur:
            if cur in seen:
                return cur
            seen.append(cur)
            cur = cur.next
            
        return None