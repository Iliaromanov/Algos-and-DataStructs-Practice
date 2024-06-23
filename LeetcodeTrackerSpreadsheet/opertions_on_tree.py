from collections import deque
class LockingTree:
    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = [[] for _ in range(len(parent))]
        for child, par in enumerate(parent):
            if par != -1:
                self.children[par].append(child)
        self.locked = [-1 for _ in range(len(parent))]

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != -1:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = -1
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num] != -1:
            return False
        cur = num
        while cur != -1:
            if self.locked[cur] != -1:
                return False
            cur = self.parent[cur]
        
        found_locked_descendant = False
        q = deque([num])
        while q:
            node = q.popleft()
            if self.locked[node] != -1:
                found_locked_descendant = True
                self.locked[node] = -1
            for child in self.children[node]:
                q.append(child)

        if found_locked_descendant is False:
            return False
        
        self.locked[num] = user
        return True