# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        right = self._getMiddleAndSplit(head)
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right)

        return self._merge(left_sorted, right_sorted)


    def _getMiddleAndSplit(self, head):
        if head.next.next is None: # only two elements
            tmp = head.next
            head.next = None
            return tmp

        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None # cut off the second half from first half

        return slow

    def _merge(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        if l1.val < l2.val:
            l1.next = self._merge(l1.next, l2)
            return l1

        l2.next = self._merge(l1, l2.next)
        return l2