#include <vector>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};


class Solution {
public:
    vector<int> postorder(Node* root) {
        if (!root) return {};
        vector<int> result;
        vector<Node*> stack{root};
        while (stack.size()) {
            Node* top = stack.back();
            if (top->children.size()) {
                for (int i = top->children.size()-1; i >= 0; --i) {
                    stack.push_back(top->children[i]);
                }
                top->children.clear();
            } else {
                result.push_back(top->val);
                stack.pop_back();
            }
        }
        return result;
    }
};
