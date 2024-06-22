"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # put first node on q
        # for len(q): create new node, 
        #   for visited neighbors add this node to them and them to this node
        #   for unvisited neighbors, put them on the q
        if not node:
            return node
        
        visited = dict() # by val: copied_node  (could do orig_node: copied_node if val not unique)
        processing = set()
        q = [node] # by node
        while q:
            top = q.pop()
            copy_node = Node(top.val, [])
            for n in top.neighbors:
                if n.val in visited:
                    visited[n.val].neighbors.append(copy_node)
                    copy_node.neighbors.append(visited[n.val])
                elif n.val not in processing:
                    processing.add(n.val)
                    q.append(n)
            visited[copy_node.val] = copy_node

        return visited[node.val]
