#include <iostream>

using namespace std;


class Node {
    public:
        int val;
        Node *next;
        Node() : val{0}, next{nullptr} {}
        Node(int val, Node *next) : val{val}, next{next} {}
};


int main() {
    Node *llist = new Node{1, new Node{2, new Node{3 , nullptr}}};
    cout << "orig list:" << endl;
    cout << llist->val << ", " << llist->next->val << ", " << llist->next->next->val << endl;


}
