///**
// * Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
// */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* result_head = head;
        ListNode* tail_of_prev_k = nullptr;
        ListNode* start;
        ListNode* end;
        start = head;
        while (start) 
        {
            // check if next k available
            int i = k;
            end = start;
            for (; i > 0; --i)
            {
                if (!end)
                {
                    start = end;
                    break;
                }
                end = end->next;
            }
            if (!start) break; // next segment len < k

            // reverse llist from start to end
            ListNode* cur = start;
            ListNode* prev = end;
            while (cur != end)
            {
                ListNode* tmp = cur->next;
                cur->next = prev;
                prev = cur;
                cur = tmp;
            }
            if (!tail_of_prev_k)
            {
                result_head = prev;
            }
            else
            {
                tail_of_prev_k->next = prev;
            }
            tail_of_prev_k = start;
            start = end;
        }
        return result_head;
    }
};
