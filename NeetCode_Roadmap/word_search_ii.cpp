class Trie {
public:
    Trie() {
        for (int i = 0; i < 26; ++i) children[i] = nullptr;
        is_end = false;
    }
    ~Trie() {
        for (int i = 0; i < 26; ++i) delete children[i];
    }

    void insert(string_view _word) {
        // cout << "adding word " << _word << " of len " << _word.length() << endl;
        Trie* cur = this; 
        int j = 0;
        for (int i = 0; i < _word.length(); ++i) {
            if (cur->get_child(_word[i]) == nullptr) {
                cur->children[_word[i]-'a'] = new Trie();
            }
            cur = cur->get_child(_word[i]);
            ++j;
        }
        cur->word = string(_word);
        cur->is_end = true;
        // cout << "   added word " << cur->word << " len " << j << endl;
    }

    Trie* get_child(char letter) {
        int idx = letter-'a';
        if (idx < 0 || idx > 25) return nullptr;
        return children[idx];
    }

    bool is_end;
    string word;
private:
    Trie* children[26];
};

class Solution {
public:
    int m, n;
    void dfs(vector<vector<char>>& board, int r, int c, Trie* cur_trie, unordered_set<string>& result) {
        if (cur_trie->is_end) {
            result.insert(cur_trie->word);
        }

        char prev = board[r][c];
        board[r][c] = '.';
        for (auto [i, j] : DIR) {
            int new_r = r + i;
            int new_c = c + j;
            if (0 <= new_r && new_r < m && 0 <= new_c && new_c < n &&
                cur_trie->get_child(board[new_r][new_c]) != nullptr)
            {
                dfs(board, new_r, new_c, cur_trie->get_child(board[new_r][new_c]), result);
            }
        }
        board[r][c] = prev;
    }

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        m = board.size();
        n = board[0].size();
        Trie t = Trie();
        for (const auto& word : words) t.insert(word);
        unordered_set<string> result;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (t.get_child(board[i][j])) {
                    dfs(board, i, j, t.get_child(board[i][j]), result);
                }
            }
        }
        return vector<string>(result.begin(), result.end());
    }

private:
    static constexpr auto DIR = {pair(1, 0), pair(0, 1), pair(-1, 0), pair(0, -1)};
};