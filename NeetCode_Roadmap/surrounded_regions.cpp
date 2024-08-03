class Solution {
public:
    void mark_uncapturable(vector<vector<char>>& board, int r, int c)
    {
        board[r][c] = 'Z';
        for (auto [i, j] : {pair(0, 1), pair(1, 0), pair(0, -1), pair(-1, 0)})
        {
            int new_r = r + i;
            int new_c = c + j;
            if (0 <= new_r && new_r < board.size() && 0 <= new_c && new_c < board[0].size() &&
                board[new_r][new_c] == 'O')
            {
                mark_uncapturable(board, new_r, new_c);
            }
        }
    }

    void solve(vector<vector<char>>& board) {   
        // left + right
        for (int i = 0; i < board.size(); ++i)
        {
            // left
            if (board[i][0] == 'O') 
                mark_uncapturable(board, i, 0);
            // right
            if (board[i][board[0].size()-1] == 'O') 
                mark_uncapturable(board, i, board[0].size()-1);
        }

        // top + bottom
        for (int i = 0; i < board[0].size(); ++i)
        {
            // top
            if (board[0][i] == 'O')
                mark_uncapturable(board, 0, i);
            // bottom
            if (board[board.size()-1][i] == 'O')
                mark_uncapturable(board, board.size()-1, i);
        }

        for (int i = 0; i < board.size(); ++i)
        {
            for (int j = 0; j < board[0].size(); ++j)
            {
                if (board[i][j] == 'O') board[i][j] = 'X';
                if (board[i][j] == 'Z') board[i][j] = 'O';
            }
        }
    }
};