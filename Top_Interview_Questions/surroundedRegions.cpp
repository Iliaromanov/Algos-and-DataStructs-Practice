class Solution {
public:
    void dfs(vector<vector<char>> &board, int row, int col) {
        vector<pair<int, int>> translations = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        board[row][col] = '1';
        for (auto trans : translations) {
            int r = row + trans.first;
            int c = col + trans.second;
            if (
                0 <= r and r < board.size() and 
                0 <= c and c < board[0].size() and
                board[r][c] == 'O'
            ) dfs(board, r, c);
        }
    }
    void solve(vector<vector<char>>& board) {
        // check at borders and mark non-flippable regions
        for (int i = 0; i < board[0].size(); ++i) {
            // top and bottom border
            if (board[0][i] == 'O') dfs(board, 0, i);
            if (board[board.size() - 1][i] == 'O') dfs(board, board.size() - 1, i);
        }
        for (int i = 0; i < board.size(); ++i) {
            // left and right border
            if (board[i][0] == 'O') dfs(board, i, 0);
            if (board[i][board[0].size() - 1] == 'O') dfs(board, i, board[0].size() - 1);
        }

        // iterate over the board, setting marked cells back to 'O' and flipping unmarked 'O' cells
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                board[i][j] = board[i][j] == '1' ? 'O' : 'X';
            }
        }
    }
};