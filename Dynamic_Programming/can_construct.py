from typing import List

def can_construct(target_word: str, word_bank: List[str]) -> bool: # O(n^m) time
    """
    Returns true if target_word can be constructed by concatenating
    strings from the word_bank
    """
    if target_word == "":
        return True

    for s in word_bank:
        if target_word.startswith(s):
            if can_construct(target_word[len(s):], word_bank):
                return True

    return False


def can_construct_memo(target_word: str, word_bank: List[str], memo = {}) -> bool: # O(m * n) time
    """
    Returns true if target_word can be constructed by concatenating
    strings from the word_bank
    """
    if target_word in memo:
        return memo[target_word]
    
    if target_word == "":
        return True

    for s in word_bank:
        if target_word.startswith(s):
            memo[target_word] = can_construct_memo(target_word[len(s):], word_bank, memo)
            if memo[target_word]:
                return True

    memo[target_word] = False
    return False      





print(can_construct_memo("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct_memo("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeeee", "eeeeeeee"]))