# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        q = [root]
        l2r = True
        while q:
            level_vals = []
            level_size = len(q)
            for _ in range(level_size):
                top = q.pop(0)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                level_vals.append(top.val)

            result.append(level_vals) if l2r else result.append(level_vals[::-1])
            l2r = not l2r

        return result
                