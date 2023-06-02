/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	a, b := headA, headB

	for a != b {
		if a == nil {
			a = headB
		} else {
			a = a.Next
		}

		if b == nil {
			b = headA
		} else {
			b = b.Next
		}
	}

	return a
}

// map solution
func getIntersectionNodeMap(headA, headB *ListNode) *ListNode {
	m := make(map[*ListNode]int)

	a, b := headA, headB

	for a != nil {
		m[a] = 1
		a = a.Next
	}

	for b != nil {
		if _, found := m[b]; found {
			return b
		}
		b = b.Next
	}
	return nil
}