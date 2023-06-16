class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> groups;
        for (string s : strs) {
            groups[getHash(s)].push_back(s);
        }
        vector<vector<string>> result;
        for (auto entry : groups) {
            result.push_back(entry.second);
        }
        return result;
    }

    string getHash(string s) {
        int arr[26] = {0};
        for (int c : s) {
            arr[c - 'a']++;
        }
        string result = "";
        for (int count : arr) {
            result += "," + to_string(count);
        }
        return result;
    }
};