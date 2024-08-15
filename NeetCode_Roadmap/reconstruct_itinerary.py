class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj = defaultdict(list)
        for src,dst in tickets:
            adj[src].append(dst)
        
        result = []
        def dfs(src):
            while adj[src]: # while still has neighbors to visit
                neighb = adj[src].pop()
                dfs(neighb)
            result.append(src)

        dfs("JFK")
        return result[::-1]
