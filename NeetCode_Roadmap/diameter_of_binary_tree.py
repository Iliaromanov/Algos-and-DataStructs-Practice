# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_depth_longest_path(node: Optional[TreeNode]) -> Tuple[int, int]:
            if node is None:
                return 0, 0
            
            md_left, lp_left = max_depth_longest_path(node.left)
            md_right, lp_right = max_depth_longest_path(node.right)

            return max(md_left, md_right)+1, max(lp_left, lp_right, md_left+md_right)

        return max_depth_longest_path(root)[1]