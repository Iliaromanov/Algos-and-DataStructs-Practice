class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        num_to_rc = {}
        for r in range(m):
            for c in range(n):
                num_to_rc[mat[r][c]] = [r,c]
        
        row_count = collections.defaultdict(lambda: n)
        col_count = collections.defaultdict(lambda: m)

        for i, num in enumerate(arr):
            r, c = num_to_rc[num]
            row_count[r] -= 1
            col_count[c] -= 1
            if row_count[r] <= 0 or col_count[c] <= 0:
                return i

        return -1
