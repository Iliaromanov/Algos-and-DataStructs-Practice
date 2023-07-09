# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0], None, None)
        root_i = inorder.index(preorder[0])
        root = TreeNode(
            preorder[0],
            self.buildTree(preorder[1:1+root_i], inorder[0:root_i]),
            self.buildTree(preorder[1+root_i:], inorder[root_i+1:])
        )
        return root