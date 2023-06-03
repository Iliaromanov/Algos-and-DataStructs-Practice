/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func reverseList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
      return head
    }
    next := head.Next
    head.Next = nil
    root := reverseList(next)
    next.Next = head
    return root
}