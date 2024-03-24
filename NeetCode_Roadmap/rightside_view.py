# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        q = collections.deque()
        q.append(root)
        while (q):
            lvl_size = len(q)
            right_side_val = -1

            for i in range(lvl_size):
                top = q.popleft()
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                right_side_val = top.val
            
            result.append(right_side_val)
        return result
            