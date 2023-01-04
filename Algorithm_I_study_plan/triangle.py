from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        known_min_paths = {}

        def backtrack(level, i):
            if level + 1 == len(triangle):
                known_min_paths[(level, i)] = triangle[level][i]
                return triangle[level][i]

            if (level, i) in known_min_paths:
                return known_min_paths[(level, i)]

            known_min_paths[(level, i)] = min(
                backtrack(level+1, i),
                backtrack(level+1, i+1)
            ) + triangle[level][i]

            return known_min_paths[(level, i)]

        return backtrack(0, 0)

        return known_min_paths[(0, 0)]