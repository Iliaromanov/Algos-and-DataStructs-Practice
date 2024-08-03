class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rem_count = 0;
        int minutes = -1;
        queue<pair<int, int>> q;
        for (int i = 0; i < grid.size(); ++i)
        {
            for (int j = 0; j < grid[0].size(); ++j)
            {
                if (grid[i][j] == 2)
                    q.push(make_pair(i, j));
                else if (grid[i][j] == 1)
                    ++rem_count;
            }
        }

        if (rem_count == 0) return 0;

        while (!q.empty())
        {
            int level_size = q.size();
            for (int k = 0; k < level_size; ++k)
            {
                auto [i, j] = q.front();
                q.pop();
                for (auto [di, dj] : {pair(0, 1), pair(1, 0), pair(0, -1), pair(-1, 0)})
                {
                    int new_i = i + di;
                    int new_j = j + dj;
                    if (0 <= new_i && new_i < grid.size() && 0 <= new_j && new_j < grid[0].size()
                        && grid[new_i][new_j] == 1)
                    {
                        grid[new_i][new_j] = 2;
                        q.push(make_pair(new_i, new_j));
                        --rem_count;
                    }
                }
            }
            ++minutes;
        }
        if (rem_count) return -1;
        return minutes;
    }
};
