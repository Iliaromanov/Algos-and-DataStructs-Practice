class Solution {
public:
    bool hasCycle(vector<vector<int>>& adj_list, vector<int>& state, int cur) {
        if (state[cur] == 1) return true;
        if (state[cur] == 0) return false;
        state[cur] = 1;
        for (auto n : adj_list[cur]) {
            if (hasCycle(adj_list, state, n)) return true;
        }
        state[cur] = 0;
        return false;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj_list(numCourses, vector<int>());
        for (const auto& vec : prerequisites) {
            int a = vec[0];
            int b = vec[1];
            adj_list[a].push_back(b);
        }
        for (int i = 0; i < numCourses; ++i) {
            vector<int> state(numCourses, -1);
            if (hasCycle(adj_list, state, i)) return false;
        }
        return true;
    }
};
