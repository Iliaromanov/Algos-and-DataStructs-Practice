# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_count = 0
        stack = [root]
        while stack:
            top = stack[-1]

            if top.left is not None:
                stack.append(top.left)
                top.left = None
                continue

            inorder_count += 1 
            stack.pop()

            if inorder_count == k:
                return top.val

            if top.right is not None:
                stack.append(top.right)

        return -1
