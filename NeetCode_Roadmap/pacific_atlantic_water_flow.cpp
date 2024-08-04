class Solution {
public:
    void dfs(vector<vector<int>>& heights, vector<vector<int>>& vis, int r, int c) {
        vis[r][c] = true;
        for (auto [i, j] : {pair(0, 1), pair(1, 0), pair(0, -1), pair(-1, 0)}) {
            int new_r = r + i, new_c = c + j;
            if (0 <= new_r && new_r < heights.size() && 0 <= new_c && 
                new_c < heights[0].size() && !vis[new_r][new_c] &&
                heights[r][c] <= heights[new_r][new_c])
            {
                dfs(heights, vis, new_r, new_c);
            }
        }
    }
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<vector<int>> pac_vis (heights.size(), vector<int>(heights[0].size(), false));
        vector<vector<int>> atl_vis (heights.size(), vector<int>(heights[0].size(), false));
        for (int i = 0; i < heights.size(); ++i)
        {
            dfs(heights, pac_vis, i, 0);  // left col
            dfs(heights, atl_vis, i, heights[0].size()-1);  // right col
        }

        for (int i = 0; i < heights[0].size(); ++i)
        {
            dfs(heights, pac_vis, 0, i); // top
            dfs(heights, atl_vis, heights.size()-1, i); // bottom
        }

        vector<vector<int>> result;
        for (int i = 0; i < heights.size(); ++i) {
            for (int j = 0; j < heights[0].size(); ++j) {
                if (pac_vis[i][j] && atl_vis[i][j])
                    result.push_back(vector<int>{i, j});
            }
        }
        return result;
    }
};