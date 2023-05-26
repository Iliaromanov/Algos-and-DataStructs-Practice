/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func sortedArrayToBST(nums []int) *TreeNode {
    if len(nums) == 0 {
        return nil
    }
    if len(nums) == 1 {
        n := TreeNode{nums[0], nil, nil};
        return &n; // in go its ok to return ref to stack variable
    }

    mid := len(nums) / 2;
    root := TreeNode{
        nums[mid], 
        sortedArrayToBST(nums[:mid]),
        sortedArrayToBST(nums[mid+1:]),
    }

    return &root;
}