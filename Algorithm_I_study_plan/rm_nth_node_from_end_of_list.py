from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        
        # move fast n spaces forward
        for i in range(n):
            fast = fast.next
        
        # n == sz when fast is None so remove first node
        if fast is None:
            return head.next
            
        # move slow and fast one node at a time until fast reaches end of list
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next  = slow.next.next if n > 1 else None
        
        return head


# Better solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head
        i = 0
        
        if not r.next:
            return None
        
        while r.next:
            if i >= n:
                l = l.next
            
            r = r.next
            i += 1
        
        if i == n - 1:
            return head.next
        
        l.next = l.next.next
        
        return head