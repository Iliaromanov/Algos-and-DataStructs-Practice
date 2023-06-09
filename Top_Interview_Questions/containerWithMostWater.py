class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_a = (r - l) * min(height[l], height[r])
        while r > l:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            max_a = max(max_a, (r - l) * min(height[l], height[r]))
        
        return max_a