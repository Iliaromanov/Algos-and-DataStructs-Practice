# LeetCode-Solutions
My solutions to LeetCode problems


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
