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


def fib_tabulation(n: int) -> int:
    """
    Returns nth fibonacci number
    """
    table = [0] * (n+1)

    if len(table) >= 2:
        table[1] = 1

    if len(table) <= 2:
        return table[n]

    for i in range(len(table)):
        if i+1 < len(table):
            table[i+1] += table[i]
        if i+2 < len(table):
            table[i+2] += table[i]

    return table[n]


print(fib(7))
print(fib_tabulation(7))