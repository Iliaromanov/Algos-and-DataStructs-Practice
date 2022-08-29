from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        def bfs(queue, visited, level):    
            l = len(queue) # number of coords at cur level
            
            for i in range(l):
                row = queue[0][0]
                col = queue[0][1]
                
                # above
                if row > 0 and (row-1, col) not in visited:
                    if mat[row-1][col] == 0:
                        return level
                    queue.append((row-1, col))
                    visited.append((row-1, col))

                # below
                if row < len(mat) - 1 and (row+1, col) not in visited:
                    if mat[row+1][col] == 0:
                        return level
                    queue.append((row+1, col))
                    visited.append((row+1, col))

                # left
                if col > 0 and (row, col-1) not in visited:
                    if mat[row][col-1] == 0:
                        return level
                    queue.append((row, col-1))
                    visited.append((row, col-1))

                # right
                if col < len(mat[0]) - 1 and (row, col+1) not in visited:
                    if mat[row][col+1] == 0:
                        return level
                    queue.append((row, col+1))
                    visited.append((row, col+1))

                # mark current coord as visited and pop it from queue
                # visited.append((row, col))
                queue.pop(0)
            
            return bfs(queue, visited, level+1)
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c]:
                    mat[r][c] = bfs([(r, c)], [(r, c)], 1)
        
        return mat
            