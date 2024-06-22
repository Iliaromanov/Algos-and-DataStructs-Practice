/*
 * Write a function that returns the path to the deepest node in a binary search tree.
 *
 *           10
 *         5    15
 *      4
 *
 *
 *
 * Result: 10, 5, 4
 */
 
class Node:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

 
def deepest_node(root: Node) -> List[int]:
    if root is None:
        return []
    
    def dfs(root: Node, path: List[int]) -> int: # [node10, [10]], [node15, [10]]
        path.append(root.val)
        if root.left is None and root.right is None:
            return 0
            
        if root.left is None:
            path_r = []
            depth = dfs(root.right, path_r)
            path.extend(path_r)
            return depth + 1
            
        if root.right is None:
            path_l = []
            depth = dfs(root.left, path_l)
            path.extend(path_l) # [4]
            return depth + 1
            
        
        path_r = [] # [15]
        depth_r = dfs(root.right, path_r)
        
        path_l = []
        depth_l = dfs(root.left, path_l)
        
        if depth_l >= depth_r:
            path.extend(path_l)
            return 1 + depth_l
        
        path.extend(path_r)
        return 1 + depth_r
    
    result = [] # []
    dfs(root, result)
    return result