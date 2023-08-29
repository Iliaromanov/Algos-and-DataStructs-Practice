# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        
        result = []
        stack = [root]
        while len(stack) > 0:
            top = stack.pop()
            if top.left is not None:
                left = top.left
                top.left = None
                stack.append(top)
                stack.append(left)
                continue

            result.append(top.val)

            if len(result) == k:
                return top.val

            if top.right is not None:
                stack.append(top.right)