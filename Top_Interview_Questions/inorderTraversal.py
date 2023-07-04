class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q = [root]

        while q:
            top = q[-1]
            if top.left is not None:
                q.append(top.left)
                top.left = None 
                continue
            
            result.append(q.pop().val)

            if top.right is not None:
                q.append(top.right)

        return result