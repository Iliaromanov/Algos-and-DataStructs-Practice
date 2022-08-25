from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        r = head
        
        if head == None or head.next == None:
            return head
        
        while r.next != None and r.next.next != None:
            l = l.next
            r = r.next.next
            
        if r.next == None:
            return l
        
        return l.next
        