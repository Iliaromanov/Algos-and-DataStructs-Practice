class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # slide rocks to right side
        for row in box:
            l, r = len(row) - 1, len(row) - 1
            while r >= 0 and row[r] != ".":
                r -= 1
            l = r-1
            while l >= 0:
                if row[l] == "#":
                    row[l] = "."
                    row[r] = "#"
                    r -= 1
                elif row[l] == "*":
                    r = l - 1
                
                l -= 1

        # do rotation
        result = []
        for col in range(len(box[0])):
            new_row = []
            for row in range(len(box)-1, -1, -1):
                new_row.append(box[row][col])
            result.append(new_row)

        return result
