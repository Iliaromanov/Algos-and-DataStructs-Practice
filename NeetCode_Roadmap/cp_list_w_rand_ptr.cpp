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

        map<Node*, Node*> copied;
        copied[head] = new Node{head->val};
        if (head->random)
            copied[head->random] = new Node{head->random->val};

        Node* new_head = copied[head];
        new_head->random = head->random ? copied[head->random] : nullptr;

        Node* cur_old = head->next; Node* cur_new = new_head;
        while (cur_old) {
            if (copied.find(cur_old) == copied.end()){
                copied[cur_old] = new Node{cur_old->val};
            }
            cur_new->next = copied[cur_old];

            if (cur_old->random and copied.find(cur_old->random) == copied.end()){
                copied[cur_old->random] = new Node{cur_old->random->val};
            }
            cur_new->next->random = cur_old->random ? copied[cur_old->random] : nullptr;

            cur_new = cur_new->next;
            cur_old = cur_old->next;
        }
        return new_head;
    }
};