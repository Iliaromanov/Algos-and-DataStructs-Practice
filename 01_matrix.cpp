#include <queue>
#include <utility>

using namespace std;

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
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
            vector<pair<int, int>> trans = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
            for (auto t : trans) {
                int row = coords.first + t.first;
                int col = coords.second + t.second;
                if (0 <= row and row < height and 0 <= col and col < width and
                    not visited[row][col])
                {
                    visited[row][col] = true;
                    mat[row][col] += mat[coords.first][coords.second];
                    q.emplace(row, col);
                }
            }
        }

        return mat;
    }
};