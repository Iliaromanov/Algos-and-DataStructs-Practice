#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int bfs(vector<vector<int>> mat, queue<pair<int, int>> visit_queue, int level) {
        int l = visit_queue.size();
        
        for (int i = 0; i < l; i++) {
            int row = visit_queue.front().first;
            int col = visit_queue.front().second;
            
            // above
            if (row > 0 and mat[row-1][col] != -1) {
                if (mat[row-1][col] == 0) {
                    return level;
                }
                visit_queue.emplace(row-1, col); // add to queue
                mat[row-1][col] = -1; // mark as visited
            }
            
            // below
            if (row < mat.size() - 1 and mat[row+1][col] != -1) {
                if (mat[row+1][col] == 0) {
                    return level;
                }
                visit_queue.emplace(row+1, col);
                mat[row+1][col] = -1;
            }
            
            // left
            if (col > 0 and mat[row][col-1] != -1) {
                if (mat[row][col-1] == 0) {
                    return level;
                }
                visit_queue.emplace(row, col-1);
                mat[row][col-1] = -1;
            }
            
            // right
            if (col < mat[0].size() - 1 and mat[row][col+1] != -1) {
                if (mat[row][col+1] == 0) {
                    return level;
                }
                visit_queue.emplace(row, col+1);
                mat[row][col+1] = -1;
            }
            
            visit_queue.pop();
        }
        
        return bfs(mat, visit_queue, level+1);
    }
    
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        for(int r = 0; r < mat.size(); r++) {
            for (int c = 0; c < mat[0].size(); c++) {
                if (mat[r][c]) {
                    queue<pair<int, int>> q;
                    q.emplace(r, c);
                    mat[r][c] = -1;
                    mat[r][c] = bfs(mat, q, 1);
                }
            }
        }
        
        return mat;
    }
};