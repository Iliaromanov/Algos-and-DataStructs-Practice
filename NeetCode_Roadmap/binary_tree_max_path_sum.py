# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPathHelper(n: TreeNode) -> Tuple[int, int]: # [ connected, disconnected ]
            if n is None:
                return [float("-inf"), float("-inf")]

            l_con, l_discon = maxPathHelper(n.left)
            r_con, r_discon = maxPathHelper(n.right)


            return (
                # CONNECTED
                max(
                    n.val,
                    l_con + n.val,
                    r_con + n.val
                ),

                #DISCONNECTED
                max(
                    # some disconnected path in left or right subtree
                    l_discon,
                    r_discon,
                    
                    # path going through n but not ending at n
                    l_con + n.val + r_con,

                    # ending before cur
                    l_con,
                    r_con
                )
            )

        return max(maxPathHelper(root))