# Algorithms Practice
My solutions to practice algorithm and data structure problems including my solutions to LeetCodes and implementations of important/notable data structures.

[My Data Structures README](Data_Structures/README.md)

## General Algorithm Templates

### Binary Search
https://leetcode.com/problems/first-bad-version/discuss/769685/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
```python
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left <= right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left # left is either index of found result or index of where the result would be located (if its not there)
```

----------------------------------------------------------------

### Backtracking
https://leetcode.com/problems/combinations/discuss/844096/Backtracking-cheatsheet-%2B-simple-solution 
```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
```

----------------------------------------------------------------

### Memoization (Top Down)
1. Make it work:
    - Visualize problem as tree
    - Implement tree using recursion
3. Make it efficient:
    - Add cache (ususally dict/hash map)
    - Add base case to return value if its in cache
    - Store result in cache before returning
    
----------------------------------------------------------------

### Tabulation (Bottom Up)
1. Visualize problem as a table
2. Size table based on inputs
3. Initialize table with default values (usually this comes down to choosing the correct type)
4. Seed the trivial answer into the table
5. Iterate through the table
6. Fill further positions in the table based on current position (to come up with this logic try to think about what options you have at each step of the problem)

----------------------------------------------------------------

### String Matching
*Let T be the string that we are searching, P be the substring/pattern whose occurence we're strying to find, and let A be all possible chars that T and P can consist of. Let n = len(T) and m = len(P). We need to return the index of the first occurence of P in T.*
#### Boyer-Moore (when all of *A* is known and of reasonably small size; eg. A={english alphabet})
**idea**: 

- let j be index in P we are currently looking at, and i be the index in T we are currently looking at.
          
- compare from end of pattern (so start at i = j = m - 1)

- let L be last occurence array/map where L[c] is the index of the last occurence of char c in P. 
  If c is not in P, L[c] = -1

- 3 Cases:
    - If T[i] not in P, then our pattern match check to start at T[i+1] (so j = m - 1, i += m)
    - If L[T[i]] < j (last occurence on the left of where we're comparing), move our pattern P so that the last occurence of T[i] in P matches with T at i.
    - If L[T[i]] > j (last occurence on the right of where we're comparing), do brute force step (just shift P one char to right and re-compare again)

**Pseudocode**:
```python
def computeL(P: str):
    L = dictionary()
    for index, char in P:
        L[char] = index
    return L
    
def matchString(T: str, P: str):
    L = computeL(P)
    i, j = m-1, m-1  # both i and j start matching from start of T at the end of P
    while i < n and j >= 0:
        if T[i] == P[j]: # matched char so decrement index at which we're checking
            i -= 1
            j -= 1
        else:
            # this formula captures all 3 cases above
            #   consult cs240 slides for further intuition
            i += m - 1 - min(L[T[i]], j - 1)
            j = m - 1
    if j == -1:
        return i+1  # found first occurence of P in T starting at i+1
    return -1  # not found
```
#### KMP (best when matching non-english alphabet chars)
----------------------------------------------------------------

### Boyer-Moore Majority Element
```python
def majorityElement(nums: List[int]) -> int:
    candidate = 0
    count = 0
    for num in nums:
        if num == candidate:
            count++
            continue
        else:
            count--
            
        if count <= 0:
            candidate = num
            count = 1
    return candidate
```
    
----------------------------------------------------------------

### Detecting Cycle in Directed Graph

```python
def detectCycle(adjacencyList: List[List[int]], n: int) -> bool:
    """
    each node in the graph is represented by an index (int)

    Args:
        n             - number of nodes in graph
        adjacencyList - adjacency list representation of a directed graph

    Returns:
        True if graph contains a cycle
        False otherwise
    """
     # state[i] = 0 (not visited) | -1 (processing) | 1 (visited/finished) 
    state = [0 for _ in range(n)]
    def hasCycle(node: int):
        if state[node] == -1:
            return True
        if state[node] == 1:
            return False

        state[node] = -1
        for outneighbor in adjacencyList[node]:
            if hasCycle(outneighbor):
                return True
        state[node] = 1
        return False

    for node in range(n):
        if hasCycle(node):
            return True
    return False
```

### Finding Topological Ordering (Kahn's algo)

```python
def getTopoOrder(adjacencyList: List[List[int]], n: int) -> List[int]:
    """
    each node in the graph is represented by an index (int)

    Args:
        n             - number of nodes in graph
        adjacencyList - adjacency list representation of a directed graph

    Returns:
        list containing the topological ordering if it exists
        empty list otherwise
    """
    inDegree = [0 for _ in range(n)]
    for node in range(n):
        for neighbour in adjacencyList(node):
            inDegree[neighbor] += 1

    que = deque()
            
    for node in range(n):
        if inDegree[node] == 0:
            que.append(node)

    topo_ordering = []
    while que:
        node = que.popleft()
        topo_ordering.append(node)
        for neighbor in adjacencyList[node]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                que.append(neighbor)

    if len(topo_ordering) == n:
        return topo_ordering
    return []
```

https://leetcode.com/problems/course-schedule/solutions/441722/python-99-time-and-100-space-collection-of-solutions-with-explanation/
    
----------------------------------------------------------------
