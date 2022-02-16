
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode *slow = head;
        ListNode *fast = head;
        while (1) {
            if (fast->next && fast->next->next) {
                slow = slow->next;
                fast = fast->next->next;
            } else if (!fast->next) {
                return slow;
            } else {
                return slow->next;
            }
        }
    }
};