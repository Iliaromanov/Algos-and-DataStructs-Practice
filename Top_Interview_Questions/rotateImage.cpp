#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int l = 0, r = matrix.size() - 1;
        while (l < r) {
            int top = l, bottom = r;
            for (int i = 0; i < r - l; ++i) {
                // save and replace top right
                int top_right = matrix[top+i][r];
                matrix[top+i][r] = matrix[top][l+i];

                // save and replace bottom right
                int bottom_right = matrix[bottom][r-i];
                matrix[bottom][r-i] = top_right;

                // save and replace bottom left
                int bottom_left = matrix[bottom-i][l];
                matrix[bottom-i][l] = bottom_right;

                // replace top left
                matrix[top][l+i] = bottom_left;
            }
            l++;
            r--;
        }
    }
};

class Solution2 {
public:
    void rotate(vector<vector<int>>& matrix) {
        reverse(matrix.begin(), matrix.end());
        for (int i = 0; i < matrix.size(); ++i) {
            for (int j = i + 1; j < matrix.size(); ++j) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};