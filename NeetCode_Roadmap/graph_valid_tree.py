class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        q = deque([0])
        while q:
            top = q.popleft()
            visited.add(top)
            for neighb in adj_list[top]:
                if neighb not in visited:
                    q.append(neighb)
        return len(edges) == n-1 and len(visited) == n
