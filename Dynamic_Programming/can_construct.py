from typing import List

def can_construct(target_word: str, word_bank: List[str]) -> bool:
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





print(can_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))