from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(r, c):
            grid[r][c] = "0"
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_r = r + i
                new_c = c + j
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) \
                  and grid[new_r][new_c] != "0":
                    dfs(new_r, new_c)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)

        return count