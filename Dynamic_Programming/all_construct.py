from typing import List

def all_construct(target: str, words: List[str]) -> List[List[str]]:
    """
    Returns all the ways target can be constructed by concatenating
    the words in words
    """
    if target == "":
        return [[]]

    combs = []
    for word in words:
        if target.startswith(word):
            comb = all_construct(target[len(word):], words)
            if comb:
                comb = [c + [word] for c in comb]
                combs.extend(comb)
    return combs


def all_construct_memo(target: str, words: List[str], memo={}) -> List[List[str]]:
    """
    Returns all the ways target can be constructed by concatenating
    the words in words
    """
    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    combs = []
    for word in words:
        if target.startswith(word):
            comb = all_construct_memo(target[len(word):], words, memo)
            if comb:
                comb = [c + [word] for c in comb]
                combs.extend(comb)

    memo[target] = combs
    return combs

print(all_construct_memo("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct_memo('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))