/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func reverseListIterative(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
      return head
    }

    var last *ListNode = nil
    cur := head
    next := head.Next
    for true {
      cur.Next = last
      last = cur
      if next == nil {
        break
      }
      cur = next
      next = next.Next
    }
    return cur
}

 func reverseListRecursive(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
      return head
    }
    next := head.Next
    head.Next = nil
    root := reverseList(next)
    next.Next = head
    return root
}