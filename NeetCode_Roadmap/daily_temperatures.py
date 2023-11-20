class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        result = [0] * len(temps)
        stack = []
        for i, t in enumerate(temps):
            while len(stack) > 0 and temps[stack[-1]] < t:
                top = stack.pop()
                result[top] = i - top
            stack.append(i)

        return result
