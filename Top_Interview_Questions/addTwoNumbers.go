/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    if l1 == nil && l2 == nil {
        return nil
    }
    head := &ListNode{}
    l1Val := 0
    l2Val := 0
    if l1 != nil {
        l1Val = l1.Val
    }
    if l2 != nil {
        l2Val = l2.Val
    }

    sum := l1Val + l2Val
    remainder := 0
    if sum >= 10 {
        sum -= 10
        remainder = 1
    }

    head.Val = sum

    if l1 == nil {
        if l2.Next != nil {
            l2.Next.Val += remainder
            head.Next = addTwoNumbers(nil, l2.Next)
        } else if remainder == 1 {
            head.Next = addTwoNumbers(&ListNode{1, nil}, nil)
        }
    } else if l2 == nil {
        if l1.Next != nil {
            l1.Next.Val += remainder
            head.Next = addTwoNumbers(l1.Next, nil)
        } else if remainder == 1 {
            head.Next = addTwoNumbers(&ListNode{1, nil}, nil)
        }
    } else {
        if remainder == 1 {
            if l1.Next != nil {
                l1.Next.Val++
                head.Next = addTwoNumbers(l1.Next, l2.Next)
            } else if l2.Next != nil {
                l2.Next.Val++
                head.Next = addTwoNumbers(l1.Next, l2.Next)
            } else {
                head.Next = addTwoNumbers(&ListNode{1, nil}, nil)
            }
        } else {
            head.Next = addTwoNumbers(l1.Next, l2.Next)
        }
    }
    return head
}