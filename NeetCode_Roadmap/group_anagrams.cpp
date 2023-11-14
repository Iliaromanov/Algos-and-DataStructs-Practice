class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        
        for (auto &word : strs) {
            int hash_list[26];
            memset(hash_list, 0, sizeof(int) * 26);
            for (char c : word) {
                hash_list[c - 'a'] += 1;
            }
            string hash_str(hash_list, hash_list + 26);
            if (groups.find(hash_str) != groups.end()) {
                groups[hash_str].push_back(word);
            } else {
                groups[hash_str] = vector<string>{word};
            }
        }

        vector<vector<string>> result;
        for (auto &entry : groups) {
            result.push_back(entry.second);
        }

        return result;
    }
};
