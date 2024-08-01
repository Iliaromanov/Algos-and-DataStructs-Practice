/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    std::unordered_map<int, Node*> cloned; // val: new_node (since val unique)
    Node* cloneGraph(Node* node) {
        if (!node) return node;
        if (cloned.contains(node->val)) return cloned[node->val];
        cloned[node->val] = new Node(node->val);
        for (auto n : node->neighbors) {
            cloned[node->val]->neighbors.push_back(cloneGraph(n));
        }
        return cloned[node->val];
    }
};