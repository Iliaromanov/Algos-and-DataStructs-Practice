class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        seen = []
        for paren in s:
            if paren in closed_to_open.values():
                seen.append(paren)
            elif ((len(seen) == 0 and paren in closed_to_open.keys()) or 
                seen.pop() != closed_to_open.get(paren)):
                return False
            
        return len(seen) == 0