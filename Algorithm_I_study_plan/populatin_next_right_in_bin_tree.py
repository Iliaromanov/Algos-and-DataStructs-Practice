from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        
        queue = [root]
        
        def bfs():
            # set next ptr of every node except rightmost
            i = 0
            while i < len(queue) - 1:
                queue[i].next = queue[i + 1]
                i += 1
                
            queue[i].next = None # rightmost's next will be null
            
            # reached leaf level
            if not queue[0].left:
                return
            
            # prepare queue for next level of tree
            i = 0
            l = len(queue)
            while i < l:
                # enqueue children
                queue.append(queue[0].left)
                queue.append(queue[0].right)
                # dequeue cur node
                queue.pop(0)
                i += 1
                
            bfs()
            
        bfs()
        
        return root