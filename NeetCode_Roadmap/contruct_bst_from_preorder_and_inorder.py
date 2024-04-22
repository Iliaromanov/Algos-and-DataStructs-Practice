# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        def makeTree(pre_start, pre_end, in_start, in_end):
            if pre_start < 0 or pre_start >= n or pre_start > pre_end:
                return None
            root_val = preorder[pre_start]
            inorder_root_i = inorder.index(root_val)
            num_left_nodes = inorder_root_i - in_start
            num_right_nodes = in_end - inorder_root_i
            return TreeNode(
                val = root_val,
                left = makeTree(
                    pre_start+1,
                    pre_start+num_left_nodes,
                    in_start,
                    inorder_root_i-1
                ),
                right = makeTree(
                    pre_start+num_left_nodes+1,
                    pre_start+num_left_nodes+num_right_nodes,
                    inorder_root_i+1,
                    in_end
                )
            )

        return makeTree(0, n-1, 0, n-1) 