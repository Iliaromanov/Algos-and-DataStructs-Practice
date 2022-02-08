package main

type ListNode struct {
    Val int
    Next *ListNode
}
 func detectCycle(head *ListNode) *ListNode {
    slow := head;
    fast := head;
    for true {
        if (slow == nil || fast == nil || fast.Next == nil) {
            return nil;
        }
        slow = slow.Next;
        fast = fast.Next.Next;
        if (slow == fast) {
            break;
        }
    }
    p := head;
    for true {
        if (p == slow) {
            break;
        }
        p = p.Next;
        slow = slow.Next;
    }
    return slow;
}