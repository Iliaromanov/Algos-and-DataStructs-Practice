from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix)-1


        while l <= r and t <= b:
           
            # top row
            for i in range(l, r+1):
                result.append(matrix[t][i])
            t += 1


            if t > b: break

            # right column
            for i in range(t, b+1):
                result.append(matrix[i][r])
            r -= 1


            if l > r: break

            # bottom row
            for i in range(r, l-1, -1):
                result.append(matrix[b][i])
            b -= 1

            if t > b: break

            # left column
            for i in range(b, t-1, -1):
                result.append(matrix[i][l])
            l += 1

        return result