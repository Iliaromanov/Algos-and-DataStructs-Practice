class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, w in times:
            adj[u].append([w, v]) # weight, neighb

        heap = [[0, k]] # minheap - [w_from_src, node]
        vis = set()
        max_w_from_k = 0
        while heap:
            parent_w, v = heapq.heappop(heap)
            max_w_from_k = max(max_w_from_k, parent_w)
            vis.add(v)
            if len(vis) == n:
                break

            for neighb_w, neighb in adj[v]:
                if neighb not in vis:
                    heapq.heappush(heap, [parent_w + neighb_w, neighb])
        
        if len(vis) < n:
            return -1

        return max_w_from_k