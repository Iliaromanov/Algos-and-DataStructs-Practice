from typing import List

def can_construct(target_word: str, word_bank: List[str]) -> bool:
    """
    Returns true if target_word can be constructed by concatenating
    strings from the word_bank
    """
    print(target_word)
    if target_word == "":
        return True


    for s in word_bank:
        if target_word.startswith(s):
            print("starts with ", s)
            if can_construct(target_word[len(s):], word_bank):
                return True
        
        if target_word.endswith(s):
            print("ends with ", s)
            if can_construct(target_word[:len(target_word) - len(s)], word_bank):
                return True

    return False           





print(can_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))