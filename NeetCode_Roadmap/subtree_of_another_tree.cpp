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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        return isSubtreePostorder(root, subRoot);
    }

    bool isSubtreePostorder(TreeNode* root, TreeNode* subRoot)
    {   
        return root->left && isSubtreePostorder(root->left, subRoot) ||
               root->right && isSubtreePostorder(root->right, subRoot) ||
               treeEqual(root, subRoot);
    }

    bool treeEqual(TreeNode* t1, TreeNode* t2)
    {
        if (!t1 || !t2)
            return !t1 && !t2;

        return t1->val == t2->val && treeEqual(t1->left, t2->left) && treeEqual(t1->right, t2->right); 
    }
};