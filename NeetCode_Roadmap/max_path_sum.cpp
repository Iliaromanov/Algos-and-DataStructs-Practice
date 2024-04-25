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
    int max_path_sum;

    int maxPathSum(TreeNode* root)
    {
        max_path_sum = root->val;
        maxGainFrmSubtree(root);
        return max_path_sum;
    }

    int maxGainFrmSubtree(TreeNode* root)
    {
        if (!root->left and !root->right)
        {
            max_path_sum = std::max(max_path_sum, root->val);
            return root->val;
        }

        int left_gain = 0;
        int right_gain = 0;
        if (root->left)
            left_gain = std::max(maxGainFrmSubtree(root->left), 0);
        if (root->right)
            right_gain = std::max(maxGainFrmSubtree(root->right), 0);

        int local_max_path_sum = left_gain + root->val + right_gain;
        max_path_sum = std::max(max_path_sum, local_max_path_sum);

        return std::max(left_gain + root->val, right_gain + root->val);
    }
};