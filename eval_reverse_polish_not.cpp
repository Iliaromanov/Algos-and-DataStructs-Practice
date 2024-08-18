#include <vector>
#include <string>
#include <functional>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stack;
        unordered_map<string, function<int(int,int)>> ops;
        ops["+"] = [](int x, int y) { return x + y; };
        ops["-"] = [](int x, int y) { return x - y; };
        ops["*"] = [](int x, int y) { return x * y; };
        ops["/"] = [](int x, int y) { return x / y; };

        for (const auto& tok : tokens) {
            if (ops.contains(tok)) {
                int rhs = stack.back();
                stack.pop_back();
                int lhs = stack.back();
                stack.pop_back();
                stack.push_back(ops[tok](lhs, rhs));
            } else {
                stack.push_back(stoi(tok));
            }
        }
        return stack[0];
    }
};