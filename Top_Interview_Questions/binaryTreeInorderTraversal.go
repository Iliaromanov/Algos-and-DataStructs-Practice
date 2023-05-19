/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func inorderTraversal(root *TreeNode) []int {
    result := make([]int, 0);
    var helper func(*TreeNode, []int) []int;
    helper = func(r *TreeNode, ans []int) []int {
        if r == nil {
            return ans;
        }
        ans = helper(r.Left, ans);
        ans = append(ans, r.Val);
        ans = helper(r.Right, ans);
        return ans;
    }
    result = helper(root, result);
    return result; 
}