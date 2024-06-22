# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        seen = []
        
        while cur:
            seen.append(cur)
            if cur.next in seen:
                return True
            cur = cur.next
            
        return False