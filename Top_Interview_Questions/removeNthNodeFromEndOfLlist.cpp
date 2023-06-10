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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == nullptr) return nullptr;
        ListNode *cur = head;
        while (n) {
            cur = cur->next;
            n--;
        }
        if (cur == nullptr) return head->next;
        ListNode *pre_del = head;
        while (cur->next) {
            pre_del = pre_del->next;
            cur = cur->next;
        }
        pre_del->next = pre_del->next->next;
        return head;
    }
};