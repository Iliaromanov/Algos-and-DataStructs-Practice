from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        _sum = 0
        carry = 0
        cur_1 = l1
        cur_2 = l2
        new_head = ListNode(0, None)
        cur = new_head
        
        while cur_1 or cur_2:
            if cur_1 and cur_2:
                _sum = (cur_1.val + cur_2.val + carry)
            elif cur_1:
                _sum = (cur_1.val + carry)
            else:
                _sum = (cur_2.val + carry)
            new_val = _sum % 10
            carry = _sum // 10
            cur.val = new_val
            if (cur_1 and cur_1.next) or (cur_2 and cur_2.next):
                cur.next = ListNode(0, None)
            elif carry:
                cur.next = ListNode(carry, None)
                break
            cur = cur.next
            cur_1 = cur_1.next if cur_1 else cur_1
                
            cur_2 = cur_2.next if cur_2 else cur_2
            
            
        return new_head