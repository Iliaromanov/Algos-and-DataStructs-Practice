class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False for _ in range(n)]
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        components_count = 0
        for node in range(n):
            if visited[node]:
                continue
            
            # bfs
            q = deque([node])
            while q:
                top = q.popleft()
                visited[top] = True
                for neighb in adj_list[top]:
                    if not visited[neighb]:
                        q.append(neighb)
            components_count += 1
        
        return components_count
