# Flood Fill solution using DFS
from typing import List, Tuple

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        visited = []
        return self.flood_fill_dfs(image, sr, sc, image[sr][sc], new_color, visited)
    
    def flood_fill_dfs(self, image: List[List[int]], row: int, col: int, old_color: int, new_color: int, visited: List[Tuple[int, int]]) -> List[List[int]]:
        image[row][col] = new_color
        height = len(image) - 1
        width = len(image[0]) - 1
        
        if (row, col) in visited:
            return image
        
        visited.append((row, col))
        
        if row and image[row - 1][col] == old_color:
            image = self.flood_fill_dfs(image, row - 1, col, old_color, new_color, visited)
        if row != height and image[row + 1][col] == old_color:
            image = self.flood_fill_dfs(image, row + 1, col, old_color, new_color, visited)
        if col and image[row][col - 1] == old_color:
            image = self.flood_fill_dfs(image, row, col - 1, old_color, new_color, visited)
        if col != width and image[row][col + 1] == old_color:
            image = self.flood_fill_dfs(image, row, col + 1, old_color, new_color, visited)
        
        return image
        