class Solution:
    def calculate(self, s: str) -> int:
        stack = collections.deque([])
        i = 0
        s = ''.join(s.split()) # remove whitespace
        # do all the * and /
        while i < len(s):
            if s[i].isdigit():
                num = ""
                while i < len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                stack.append(int(num))
                i -= 1
            elif s[i] in "-+":
                stack.append(s[i]) 
            elif s[i] in "*/":
                op = s[i]
                lhs = int(stack.pop())
                rhs = ""
                i += 1
                while i < len(s) and s[i].isdigit():
                    rhs += s[i]
                    i += 1
                rhs = int(rhs)
                result = int(lhs/rhs) if op == "/" else lhs*rhs
                stack.append(result)
                i -= 1
            i += 1
        
        # do all + and - starting at lhs
        while len(stack) > 1:
            lhs, op, rhs = int(stack.popleft()), stack.popleft(), int(stack.popleft())
            result = lhs + rhs if op == "+" else lhs - rhs
            stack.appendleft(result)

        return int(stack.pop())