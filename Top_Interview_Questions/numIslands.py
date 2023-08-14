class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def removeIsland(r, c):
            grid[r][c] = "0"
            for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                new_r, new_c = r + i, c + j
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) \
                   and grid[new_r][new_c] == "1":
                    removeIsland(new_r, new_c)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    removeIsland(row, col)
        
        return count