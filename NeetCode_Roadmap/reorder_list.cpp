/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head or !head->next) return;
        ListNode* left = head; ListNode* right = head;
        
        while (right and right->next and right->next->next) {
            left = left->next;
            right = right->next->next;
        }

        right = left->next;
        left->next = nullptr;

        ListNode* prev = nullptr;
        ListNode* cur = right;
        while (cur) {
            ListNode* tmp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = tmp;
        }

        left = head->next; right = prev;
        cur = head;
        int use_left = 0;
        while (left or right) {
            if (use_left) {
                cur->next = left;
                left = left->next;
            } else {
                cur->next = right;
                right = right->next;
            }

            use_left = 1 - use_left;
            cur = cur->next;
        }
    }
};
