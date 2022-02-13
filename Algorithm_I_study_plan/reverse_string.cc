#include <vector>

class Solution {
public:
    void reverseString(vector<char>& s) {
        int l = 0;
        int r = s.size() - 1;
        while (l <= r) {
            char tmp = s.at(r);
            s[r--] = s[l];
            s[l++] = tmp;
        }
    }
};