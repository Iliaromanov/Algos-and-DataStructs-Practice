# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not (root1 or root2): return None
        
        result_root = TreeNode(0, None, None) 
        if root1 and root2:
            result_root.val = root1.val + root2.val
            result_root.left = self.mergeTrees(root1.left, root2.left)
            result_root.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            result_root.val = root1.val
            result_root.left = self.mergeTrees(root1.left, None)
            result_root.right = self.mergeTrees(root1.right, None)
        else:
            result_root.val = root2.val
            result_root.left = self.mergeTrees(None, root2.left)
            result_root.right = self.mergeTrees(None, root2.right)
        
        return result_root


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        elif not root1:
            return root2
        elif not root2:
            return root1

        new_root = TreeNode(
            root1.val + root2.val,
            self.mergeTrees(root1.left, root2.left),
            self.mergeTrees(root1.right, root2.right)
        )

        return new_root