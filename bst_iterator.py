from typing import Optional, List
# Definition for a binary tree node.
# [7, 3, 15, null, null, 9, 20]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self, vals: List[int]):
        self.root = None
        for val in vals:
            self.insert(val)

    def insert(self, val: int):
        if self.root is None:
            self.root = TreeNode(val)
            return
        
        def insert_recursive(val: int, cur_node: TreeNode):
            if val < cur_node.val:
                if cur_node.left:
                    insert_recursive(val, cur_node.left)
                else:
                    cur_node.left = TreeNode(val)
                    return
            else:
                if cur_node.right:
                    insert_recursive(val, cur_node.right)
                else:
                    cur_node.right = TreeNode(val)
                    return
        
        insert_recursive(val, self.root)

    @staticmethod
    def get_inorder(root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        def inorder_helper(cur_node: TreeNode):
            if cur_node.left is not None:
                inorder_helper(cur_node.left)
            result.append(cur_node.val)
            if cur_node.right is not None:
                inorder_helper(cur_node.right)
        
        inorder_helper(root)
        return result
            

bst = BST([7, 3, 15, 9, 20])
        
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self._inorder = BST.get_inorder(root)
        print(f'self inorder: {self._inorder}')
        self._cur_i = -1
        self._has_next = True

    def next(self) -> int:
        self._cur_i += 1
        if self._cur_i == len(self._inorder) - 1:
            self._has_next = False
        return self._inorder[self._cur_i]

    def hasNext(self) -> bool:
        return self._has_next


it = BSTIterator(bst.root)
for _ in range(5):
    print(it.next())
    print(it.hasNext())


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()