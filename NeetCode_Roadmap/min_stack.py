class Node:
    def __init__(self, val: int, min_val: int, next_n):
        self.val = val
        self.min_val = min_val
        self.next_n = next_n

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head is not None:
            self.head = Node(
                val, min(self.head.min_val, val),
                self.head
            )
        else:
            self.head = Node(val, val, None)

    def pop(self) -> None:
        self.head = self.head.next_n

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min_val
