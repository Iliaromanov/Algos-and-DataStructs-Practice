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


print(count_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))
print(count_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl'])) 