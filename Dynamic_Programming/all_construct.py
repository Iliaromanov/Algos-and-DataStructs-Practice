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




print(all_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))