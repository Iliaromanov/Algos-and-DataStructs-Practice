/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        std::vector<vector<int>> result;
        if (!root) 
            return result;
        std::deque<TreeNode*> q = {root};
        while (!q.empty())
        {
            std::vector<int> level;
            for (int lvl_size = q.size(); lvl_size > 0; --lvl_size)
            {
                TreeNode* front = q.front();
                if (front->left)
                    q.push_back(front->left);
                if (front->right)
                    q.push_back(front->right);
                level.push_back(front->val);
                q.pop_front();
            }
            result.push_back(level);
        }
        return result;
    }
};