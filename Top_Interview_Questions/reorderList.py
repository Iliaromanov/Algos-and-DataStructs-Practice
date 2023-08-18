# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head

        # get middle
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        left, right = head, slow.next
        slow.next = None  # separate left and right

        # reverse 2nd half of llist
        prev = None
        cur = right
        while cur is not None:
            tmp_next = cur.next
            cur.next = prev
            prev = cur
            cur = tmp_next
        right = prev

        # merge the two lists
        left_turn = True
        while left is not None: # left will always be longer or equal
            if left_turn:
                tmp = left.next
                left.next = right
                left = tmp
            else:
                tmp = right.next
                right.next = left
                right = tmp

            left_turn = not left_turn

        return head

