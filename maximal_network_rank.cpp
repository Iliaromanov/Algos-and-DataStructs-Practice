class Solution {
public:
    int rank(int v1, int v2, vector<unordered_set<int>> &adj_list)
    {
        if (v1 == v2) return 0;
        int result = adj_list.at(v1).size() + adj_list.at(v2).size();
        if (adj_list.at(v1).find(v2) != adj_list.at(v1).end())
            return result - 1;
        return result;
    }
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        // build adjacency list
        vector<unordered_set<int>> adj_list(n);
        for (auto& pair : roads)
        {
            adj_list[pair[0]].insert(pair[1]);
            adj_list[pair[1]].insert(pair[0]);
        }

        // iterate over adjacency list and find pair with max rank
        int max_rank = 0;
        for (int v1 = 0; v1 < n; v1++)
        {
            for (int v2 = 0; v2 < n; v2++)
            {
                if (v1 == v2) continue;
                max_rank = std::max(max_rank, rank(v1, v2, adj_list));
            }
        }
        return max_rank;
    }
};