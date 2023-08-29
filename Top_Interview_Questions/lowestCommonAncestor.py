# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getPath(cur_n, target):
            if cur_n == target:
                return [target]
            left = []
            if cur_n.left:
                left = getPath(cur_n.left, target)
            right = []
            if cur_n.right:
                right = getPath(cur_n.right, target)
            
            if not left and not right:
                return []
  
            return [cur_n] + left if left else [cur_n] + right 

        p_path = getPath(root, p)
        q_path = getPath(root, q)

        i = 0
        while i < len(p_path) and i < len(q_path) and p_path[i] == q_path[i]:
            i += 1

        return p_path[i - 1]