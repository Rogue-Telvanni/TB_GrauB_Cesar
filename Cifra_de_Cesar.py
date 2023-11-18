alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
length = len(alphabet)


def cipher_word(word: str, key: int) -> str:
    code = ''
    for char in word:
        code += next_char(char, key)
    return code


def next_char(char: str, key: int) -> str:
    index = alphabet.index(char)
    pos = index + key
    while pos >= length:
        pos = pos - length

    return alphabet[pos]


def decipher_word(word: str, key: int) -> str:
    code = ''
    for char in word:
        code += previous_char(char, key)
    return code


def previous_char(char: str, key: int) -> str:
    index = alphabet.index(char)
    pos = index - key
    while pos < 0:
        pos = length + pos

    return alphabet[pos]


def brute_force_text(word: str, hash_set: set) -> (int, str):
    key = 1
    size = len(word)
    while key < 100000:
        print(f"testando chave {key}")
        # descriptografa somente uma palavra
        test = ""
        for i in range(size):
            piece = previous_char(word[0 + i: i + 1], key)
            test += piece

        if test in hash_set:
            return key, test

        key += 1

    return key, "erro"


def brute_force(word: str, hash_set: set) -> (int, str):
    key = 1
    size = len(word)
    while key < 100000:
        print(f"testando chave {key}")
        # descriptografa somente uma palavra
        test = ""
        for i in range(size):
            piece = previous_char(word[0 + i: i + 1], key)
            test += piece

        if test in hash_set:
            return key, test

        key += 1

    return key, "erro"