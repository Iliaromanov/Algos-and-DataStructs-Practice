class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-/*":
                rhs = int(stack.pop())
                lhs = int(stack.pop())
                match token:
                    case "+":
                        stack.append(lhs + rhs)
                    case "-":
                        stack.append(lhs - rhs)
                    case "/":
                        stack.append(int(lhs / rhs))
                    case _:
                        stack.append(lhs * rhs)
            else:
                stack.append(int(token))
        return stack[0]