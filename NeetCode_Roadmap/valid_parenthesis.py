class Solution:
    def isValid(self, s: str) -> bool:
        open2close = {
            "(": ")", "[": "]", "{": "}"
        }
        stack = []
        for c in s:
            if c in open2close.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or open2close[stack[-1]] != c:
                    return False
                stack.pop()

        return len(stack) == 0
                    
