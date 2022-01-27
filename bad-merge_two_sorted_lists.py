from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        
        if not cur1:
            return cur2
        if not cur2:
            return cur1
        
        if cur1.val < cur2.val:
            head = cur1
            cur1 = cur1.next
        else:
            head = cur2
            cur2 = cur2.next
        cur = ListNode(head.val, None)
        head = cur
        
        while cur1 and cur2:
            print(f"cur1: {cur1.val}, cur2: {cur2.val}")
            if cur1.val < cur2.val:
                cur.next = ListNode(cur1.val, None)
                cur1 = cur1.next
            else:
                cur.next = ListNode(cur2.val, None)
                cur2 = cur2.next
                
            cur = cur.next 
        
        if cur:
            cur.next = cur1 if cur1 else cur2
            
        return head