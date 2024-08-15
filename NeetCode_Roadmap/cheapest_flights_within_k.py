class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        dist = [float('inf')] * (n+1)
        dist[src] = 0
        for u, v, p in flights:
            adj[u].append([v, p])
        
        q = deque([[src, 0, 0]])
        vis = set()
        while q:
            top, hops_top, dist_top = q.popleft()
            # print(f"top: {top}, hops: {hops_top}")
            vis.add(top)
            for n, p in adj[top]:
                if dist_top + p < dist[n] and hops_top <= k:
                    dist[n] = dist_top + p
                    # print(f"     updating neighb: {n} to {dist[n]}")
                    q.append([n, hops_top+1, dist_top+p])

        if dst not in vis:
            return -1

        return dist[dst]
