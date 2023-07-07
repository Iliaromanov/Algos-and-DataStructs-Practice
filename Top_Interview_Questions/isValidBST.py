# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        prev = None
        while stack:
            top = stack[-1]
            if top.left is not None:
                stack.append(top.left)
                top.left = None
                continue

            cur = stack.pop().val
            if prev is not None and cur <= prev:
                return False
            prev = cur

            if top.right is not None:
                stack.append(top.right)

        return True
    
    
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidSubBST(root: Optional[TreeNode], local_min: Optional[int], local_max: Optional[int]):
            if root is None: return True
            return (
                (local_min is None or local_min < root.val) and (local_max is None or root.val < local_max)
                and isValidSubBST(
                    root.left, local_min, root.val if local_max is None else min(root.val, local_max)
                )
                and isValidSubBST(
                    root.right, root.val if local_min is None else max(root.val, local_min), local_max
                )
            )
        return (isValidSubBST(root.left, None, root.val) and 
                isValidSubBST(root.right, root.val, None))
    
