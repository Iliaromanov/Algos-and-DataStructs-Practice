class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-/*":
                rhs = stack.pop()
                lhs = stack.pop()
                if token == "+":
                    stack.append(lhs+rhs)
                elif token == "-":
                    stack.append(lhs-rhs)
                elif token == "*":
                    stack.append(lhs*rhs)
                else:
                    stack.append(int(lhs / rhs))
            else:
                stack.append(int(token))

        return stack[0]
