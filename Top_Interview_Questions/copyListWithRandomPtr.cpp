/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;
        map<Node *, Node *> seen;
        Node *cur_old = head;
        Node *cur_new = new Node(head->val);
        seen[head] = cur_new;
        while (cur_old) {
            if (seen.find(cur_old->next) != seen.end()) {
                cur_new->next = seen[cur_old->next];
            } else if (cur_old->next) {
                cur_new->next = new Node(cur_old->next->val);
                seen[cur_old->next] = cur_new->next;
            }

            if (seen.find(cur_old->random) != seen.end()) {
                cur_new->random = seen[cur_old->random];
            } else if (cur_old->random) {
                cur_new->random = new Node(cur_old->random->val);
                seen[cur_old->random] = cur_new->random;
            }
            cur_old = cur_old->next;
            cur_new = cur_new->next;
        }
        return seen[head];
    }
};