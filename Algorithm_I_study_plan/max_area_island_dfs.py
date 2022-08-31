from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        
        def _dfs_get_size(grid: List[List[int]], row: int, col: int, island_size: int) -> int:
            grid[row][col] = 0
            size = island_size + 1
            
            if row and grid[row - 1][col]:
                size += _dfs_get_size(grid, row - 1, col, island_size)
            if row != height - 1 and grid[row + 1][col]:
                size += _dfs_get_size(grid, row + 1, col, island_size)
            if col and grid[row][col - 1]:
                size += _dfs_get_size(grid, row, col - 1, island_size)
            if col != width - 1 and grid[row][col + 1]:
                size += _dfs_get_size(grid, row, col + 1, island_size)
 
            return size
        
        max_size = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    island_size = _dfs_get_size(grid, row, col, 0)
                    if island_size > max_size:
                        max_size = island_size
                        
        return max_size
            

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        width = len(grid)
        height = len(grid[0])
        
        def dfs(row, col, area):
            grid[row][col] = 0
            
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r = row + i
                new_c = col + j
                
                if 0 <= new_r < width and 0 <= new_c < height and grid[new_r][new_c]:
                    area += dfs(new_r, new_c, 1)
                    
            return area
        
        for r in range(width):
            for c in range(height):
                if grid[r][c]:
                    a = dfs(r, c, 1)
                    if a > max_area:
                        max_area = a
                        
        return max_area