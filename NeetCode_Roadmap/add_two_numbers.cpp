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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* result = new ListNode();
        ListNode* result_head = result;
        
        int carry = 0;
        ListNode* l1_cur = l1; ListNode* l2_cur = l2;
        while (l1_cur or l2_cur) {
            int sub_result = carry;
            if (l1_cur) {
                sub_result += l1_cur->val;
            } 
            if (l2_cur) {
                sub_result += l2_cur->val;
            }
            result->next = new ListNode(sub_result % 10);
            result = result->next;
            carry = sub_result / 10;
            if (l1_cur) l1_cur = l1_cur->next;
            if (l2_cur) l2_cur = l2_cur->next;
        }
        
        if (carry) result->next = new ListNode(1);

        return result_head->next;
    }
};
