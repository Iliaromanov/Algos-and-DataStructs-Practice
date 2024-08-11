class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        num levels in topo sort
        """
        # get indeg
        indeg = defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for di, dj in [[0,1], [1,0], [0,-1],[-1,0]]:
                    new_i = i + di
                    new_j = j + dj
                    if (0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and 
                       matrix[new_i][new_j] > matrix[i][j]):
                        indeg[(new_i,new_j)] += 1


        # get topo and start states
        q = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if indeg[(i,j)] == 0:
                    q.append((i,j))

        topo = []
        DIR = [[0,1], [1,0], [0,-1],[-1,0]]
        l = 0
        while len(q):
            lev_size = len(q)
            for _ in range(lev_size):
                top = q.popleft()
                i,j = top
                topo.append(top)
                assert(len(indeg) <= len(matrix) * len(matrix[0]), indeg)
                for di, dj in DIR:
                    new_i = i + di
                    new_j = j + dj
                    if (0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and 
                        matrix[new_i][new_j] > matrix[i][j]):
                        indeg[(new_i, new_j)] -= 1
                        if indeg[(new_i, new_j)] == 0:
                            q.append((new_i, new_j))
            l += 1

        return l


        
