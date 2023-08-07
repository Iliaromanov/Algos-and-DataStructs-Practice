class Node {
    public:
        Node() : val{0}, min{0}, next{nullptr} {}
        Node(int val, int min) : val{val}, min{min}, next{nullptr} {}
        Node(int val, int min, Node *next) : val{val}, min{min}, next{next} {}

        int val;
        int min;
        Node *next;
};

class MinStack {
public:
    void push(int val) {
        if (!head) {
            head = new Node{val, val};
        } else {
            head = new Node{val, min(val, head->min), head};
        }
    }
    
    void pop() {
        head = head->next;
    }
    
    int top() {
        return head->val;
    }
    
    int getMin() {
        return head->min;
    }

private:
    Node *head;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */