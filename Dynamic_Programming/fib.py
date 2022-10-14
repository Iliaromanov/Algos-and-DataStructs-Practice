# dynmic programming excercise solving fib

def fib(n: int) -> int:
    """
    Returns nth fibonacci number
    """
    solved = {}

    def fib_helper(n: int) -> int:
        if n <= 2:
            return 1

        if n in solved:
            return solved[n]

        solved[n] = fib_helper(n-1) + fib_helper(n-2)

        return solved[n]
    
    return fib_helper(n)


print(fib(7))