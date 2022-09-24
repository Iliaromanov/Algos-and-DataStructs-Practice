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


# slightly cleaner solution
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        to_rot_count = 0
        queue = []
        visited = set()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    to_rot_count += 1
        
        # bfs
        l = len(queue)
        while queue:
            
            if to_rot_count == 0:
                return minutes
            
            minutes += 1
            l = len(queue)
            while l:
                r, c = queue.pop(0)

                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_r = r + y
                    new_c = c + x

                    if 0 <= new_r < len(grid) and \
                       0 <= new_c < len(grid[0]) and (new_r, new_c) not in visited \
                       and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))
                        to_rot_count -= 1
                        visited.add((new_r, new_c))
                l -= 1
        
        if to_rot_count:
            return -1
        return minutes
 