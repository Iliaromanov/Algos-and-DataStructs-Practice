class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for cur_i, cur_h in enumerate(heights + [0]): # need 0 at the end to pop off remaining heights
            i = cur_i
            while stack and stack[-1][1] > cur_h:
                i, h = stack.pop()
                # h = heights[i]
                # max block area of rect of height h up to cur_i
                local_max_area = (cur_i - i) * h
                max_area = max(local_max_area, max_area)
            
            stack.append((i, cur_h))

        return max_area