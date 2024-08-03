class Solution {
public:
    int bfs(vector<vector<int>>& grid, int r, int c) {
        std::pair<int, int> dir[] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        std::queue<std::pair<int, int>> q(std::make_pair(r, c));
        std::unordered_set<string> visited = to_string;
        while (q.empty()) {
            auto [i, j] = q.front();
            q.pop_front();
            if 
        }
    }

    void islandsAndTreasure(vector<vector<int>>& grid) {
        
    }
};
