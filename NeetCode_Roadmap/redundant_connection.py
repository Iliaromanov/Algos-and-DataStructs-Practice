class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i:i for i in range(1, len(edges)+1)}
        size = {i:0 for i in range(1, len(edges)+1)}
        def find(x: int) -> int:
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union_by_size(x: int, y: int) -> bool:
            """returns true if already unioned else false
            """
            x_rep = find(x)
            y_rep = find(y)
            if x_rep == y_rep:
                return True
            
            if size[x_rep] < size[y_rep]:
                parent[x_rep] = y_rep
                size[y_rep] += size[x_rep]
            else:
                parent[y_rep] = x_rep
                size[x_rep] += size[y_rep]
            
            return False

        for a, b in edges:
            if union_by_size(a, b):
                return [a, b]
            