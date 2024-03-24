# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, cur_max: int) -> int:
            if root is None:
                return 0

            if root.val >= cur_max:
                cur_max = max(root.val, cur_max)
                return dfs(root.left, cur_max) + dfs(root.right, cur_max) + 1
            
            return dfs(root.left, cur_max) + dfs(root.right, cur_max)

        return dfs(root, root.val)
            

        