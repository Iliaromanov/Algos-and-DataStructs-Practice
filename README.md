# Algorithms Practice
My solutions to practice algorithm and data structure probles including my solutions to LeetCode problems


## General Ideas/Templates

### Binary Search
https://leetcode.com/problems/first-bad-version/discuss/769685/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
```python
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
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

### Memoization
1. Make it work:
    - Visualize problem as tree
    - Implement tree using recursion
3. Make it efficient:
    - Add cache (ususally dict/hash map)
    - Add base case to return value if its in cache
    - Store result in cache before returning
    
----------------------------------------------------------------

## Tabulation
1. Visualize problem as a table
2. Size table based on inputs
3. Initialize table with default values (usually this comes down to choosing the correct type)
4. Seed the trivial answer into the table
5. Iterate through the table
6. Fill further positions in the table based on current position (to come up with this logic try to think about what options you have at each step of the problem)

