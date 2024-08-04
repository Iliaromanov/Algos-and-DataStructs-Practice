class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        int N = numCourses;
        vector<vector<int>> adj_list(N, vector<int>());
        vector<int> indegree(N, 0);
        for (const auto& vec : prerequisites) {
            int a = vec[0], b = vec[1];
            adj_list[b].push_back(a);
            ++indegree[a];
        }
        std::queue<int> q;
        for (int n = 0; n < N; ++n) {
            if (indegree[n] == 0) q.push(n);
        }
        std::vector<int> topo_sort;
        while (!q.empty()) {
            int top = q.front();
            q.pop();
            topo_sort.push_back(top);
            for (const auto neighbor : adj_list[top]) {
                if (--indegree[neighbor] == 0) q.push(neighbor);
            }
        }
        if (topo_sort.size() != N) return vector<int>();
        return topo_sort;
    }
};