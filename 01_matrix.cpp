#include <queue>
#include <utility>

using namespace std;

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        vector<int> DIR = {0, 1, 0, -1, 0};
        int height = mat.size();
        int width = mat[0].size();
        vector<vector<bool>> visited(height, vector<bool>(width, false));
        queue<pair<int, int>> q;

        for (int i = 0; i < height; ++i) {
            for (int j = 0; j < width; ++j) {
                if (not mat[i][j]) {
                    visited[i][j] = true;
                    q.emplace(i, j);
                }
            }
        }

        while (not q.empty()) {
            pair<int, int> coords = q.front();
            q.pop();
            for (int i = 0; i < 4; ++i) {
                int row = coords.first + DIR[i];
                int col = coords.second + DIR[i+1];
                if (0 <= row and row < height and 0 <= col and col < width and
                    not visited[row][col])
                {
                    visited[row][col] = true;
                    mat[row][col] = mat[coords.first][coords.second] + 1;
                    q.emplace(row, col);
                }
            }
        }

        return mat;
    }
};