class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        grid_max = 0
        for i, j in product(range(n), range(n)):
            grid_max = max(grid_max, grid[i][j])

        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(x, y, t, vis) -> bool:
            """
            returns true if grid[n-1][n-1] can be reached from grid[x][y]
            only using nodes of height t
            """
            vis.add(grid[x][y])
            if x == n-1 and y == n-1:
                return True

            for i, j in DIR:
                new_x, new_y = x + i, y + j
                if (0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] not in vis and
                   grid[new_x][new_y] <= t and dfs(new_x, new_y, t, vis)):
                    return True

            return False

        l, r = 0, grid_max
        while l <= r:
            m = l + (r-l) // 2
            vis = set([grid[0][0]])
            if grid[0][0] <= m and dfs(0, 0, m, vis):
                r = m-1
            else:
                l = m+1

        return l
                     