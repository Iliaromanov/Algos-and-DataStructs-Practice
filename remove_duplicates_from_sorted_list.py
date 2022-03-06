from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        seen = [head.val]
        fast = head.next
        slow = head
        while fast:
            if fast.val in seen:
                slow.next = fast.next
            else:
                seen.append(fast.val)
                slow = slow.next
                
            fast = fast.next
            
            
        return head