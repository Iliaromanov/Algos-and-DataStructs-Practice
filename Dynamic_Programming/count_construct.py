from typing import List

def count_construct(target: str, words: List[str]) -> int:
    """
    Returns the number of ways target can be constructed by
    concatenating strings from words
    """
    
    if target == "":
        return 1

    count = 0
    for word in words:
        if target.startswith(word):
            count += count_construct(target[len(word):], words)

    return count


def count_construct_memo(target: str, words: List[str], memo={}) -> int:
    """
    Returns the number of ways target can be constructed by
    concatenating strings from words
    """
    if target in memo:
        return memo[target]
    
    if target == "":
        return 1

    count = 0
    for word in words:
        if target.startswith(word):
            count += count_construct_memo(target[len(word):], words, memo)

    memo[target] = count
    return count



print(count_construct_memo("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))
print(count_construct_memo("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
print(count_construct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeeee", "eeeeeeee"]))