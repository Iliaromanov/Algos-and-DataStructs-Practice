class Solution {
public:
    int trap(vector<int>& height) {
        int total = 0;
        int subtotal = 0;
        int cur_start_i = 0;
        int s = height.size();
        for (int i = 0; i < s; ++i) {
            if (height[i] >= height[cur_start_i]) {
                cur_start_i = i;
                total += subtotal;
                subtotal = 0;
            } else {
                subtotal += height[cur_start_i] - height[i];
            }
        }

        if (cur_start_i == s - 1) return total;
        
        int back_start_i = s - 1;
        for (int i = s - 1; i > cur_start_i; --i) {
            if (height[back_start_i] <= height[i]) back_start_i = i;
            else total += height[back_start_i] - height[i];
        }
        return total;
    }
};
