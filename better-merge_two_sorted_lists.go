package main;

type ListNode struct {
    Val int
    Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    // Return the other list if one of them is empty
    if (list1 == nil) { return list2; }
    if (list2 == nil) { return list1; }
    
    // Determine head of merged list
    var head *ListNode;
    if (list1.Val < list2.Val) {
        head = list1;
        list1 = list1.Next;
    } else {
        head = list2;
        list2 = list2.Next;
    }
    cur := head;
    
    // Merge the remainder of the lists until all nodes of one of the lists
    //  have been used
    for (list1 != nil && list2 != nil) {
        if (list1.Val < list2.Val) {
            if (cur.Next != list1) {
                cur.Next = list1;
            }
            list1 = list1.Next;
        } else {
            if (cur.Next != list2) {
                cur.Next = list2;
            }
            list2 = list2.Next;
        }
        cur = cur.Next;
    }
    
    // Append the remaning nodes
    if (list2 == nil) {
        cur.Next = list1;
    } else {
        cur.Next = list2;
    }
    
    return head; 
}
