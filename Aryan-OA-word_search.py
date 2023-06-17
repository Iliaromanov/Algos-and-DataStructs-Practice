def word_match(pattern: str, word: str) -> bool:
    """
    Helper func that returns tru when word matches pattern
    """
    i = 0
    for j, char in enumerate(pattern):
        if char == '?':
            word[i] = '?'
        elif char == "*" and j != len(pattern) - 1:
            word = word.replace(word[i:word.index(pattern[j+1])], "*", 1)
        i += 1

    print(word)

    if pattern != word:
        return False

    return True


def search(pattern: str, dictionary: list) -> list:
    result = []
    for word in dictionary:
        if word_match(pattern, word):
            result.append(word)

    return result


print(word_match("p*y", "pretty"))