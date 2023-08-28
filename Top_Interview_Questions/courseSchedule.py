class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for c1, c2 in prerequisites:
            # c1 -> c2 is an edge
            adjList[c1].append(c2)

        # state[i] = 0 (not visited) | -1 (processing) | 1 (visited/finished) 
        state = [0 for _ in range(numCourses)]

        def hasCycle(i):
            # still processing means we found cycle containing ci
            if state[i] == -1:
                return True

            # ci already visited, no need to dfs
            if state[i] == 1:
                return False 
            
            state[i] = -1
            for dep in adjList[i]:
                if hasCycle(dep):
                    return True
            state[i] = 1
            return False

        for ci in range(numCourses):
            if hasCycle(ci):
                return False # if cycle involving course, then can't finish

        return True