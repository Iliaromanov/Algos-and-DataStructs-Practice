class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for c1, c2 in prerequisites:
            # c2-> is edge
            adjList[c2].append(c1)
            in_degree[c1] += 1
        
        q = collections.deque([])

        for ci in range(numCourses):
            if in_degree[ci] == 0:
                q.append(ci)

        topo_ordering = []
        while q:
            ci = q.popleft()
            topo_ordering.append(ci)
            for neighbor in adjList[ci]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        if len(topo_ordering) != numCourses:
            return []
        return topo_ordering

