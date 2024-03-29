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

# BFS
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left:
            return root

        queue = [root]

        while queue:
            cur_size = len(queue)
            for i in range(cur_size):
                cur = queue.pop(0)
                if i < cur_size - 1:
                    cur.next = queue[0]

                if cur.left:
                    queue.append(cur.left)
                    queue.append(cur.right)
        
        return root

 # DFS
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left:
            return root

        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root
