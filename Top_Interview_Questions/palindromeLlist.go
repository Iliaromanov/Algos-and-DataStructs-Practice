/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func isPalindrome(head *ListNode) bool {
    if head == nil || head.Next == nil {
      return true
    }

    // get middle node
    slow, fast := head, head
    for fast != nil && fast.Next != nil {
      slow = slow.Next
      fast = fast.Next.Next
    }

    // reverse list starting from middle
    var last *ListNode = nil
    cur := slow
    next := slow.Next
    for true {
      cur.Next = last
      last = cur
      if next == nil {
        break
      }
      cur = next
      next = next.Next
    }

    // check for palindrome
    left, right := head, cur
    for true {
      if left.Val != right.Val {
        return false
      }
      if left.Next == nil || right.Next == nil {
        break
      }
      left = left.Next
      right = right.Next
    }
    return true
}