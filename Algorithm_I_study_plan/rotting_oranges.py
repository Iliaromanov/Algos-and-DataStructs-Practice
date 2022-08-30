from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        width = len(grid)
        height = len(grid[0])
        to_visit_count = width * height
        visited_count = 0
        steps_count = 0
        
        queue = []
        
        # do to_visit -= 1 for every 0 and visited += 1 for every 2
        for r in range(width):
            for c in range(height):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited_count += 1
                elif grid[r][c] == 0:
                    to_visit_count -= 1
                    
        
        if visited_count == to_visit_count:
                return steps_count
        
                    
        while queue:
            l = len(queue)
            for _ in range(l):
                r, c = queue.pop(0)
                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_r = r + i
                    new_c = c + j
                    
                    if 0 <= new_r < width and 0 <= new_c < height and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))
                        visited_count += 1
            
            steps_count += 1
            
            if visited_count == to_visit_count:
                return steps_count
            
        return -1
