class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        std::vector<std::pair<int, int>> dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (int i = 0; i < board.size(); ++i)
        {
            for (int j = 0; j < board[0].size(); ++j)
            {
                if (board[i][j] == word[0] && word_found(board, word, 1, i, j, dir))
                    return true;
            }
        }
        return false;
    }

    bool word_found(vector<vector<char>>& board, const string& word, int word_i, int r, int c, const std::vector<std::pair<int, int>>& dir)
    {
        if (word_i == word.length())
            return true;
        
        char prev = board[r][c];
        board[r][c] = '0';

        for (const auto& [i, j] : dir)
        {
            int new_r = r + i;
            int new_c = c + j;

            if (0 <= new_r && new_r < board.size() && 0 <= new_c && new_c < board[0].size() && 
                word[word_i] == board[new_r][new_c] && word_found(board, word, word_i+1, new_r, new_c, dir))
            {
                return true;
            }
        }

        board[r][c] = prev;

        return false;
    }
};