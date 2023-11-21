# alfabeto usado para criptografia e descriptografia
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
length = len(alphabet)

"""cifra a palavra enviada com a chave passada para o método"""


def cipher_word(word: str, key: int) -> str:
    code = ''
    # para cada letra, busca a próxima letra com base na chave
    for char in word:
        code += next_char(char, key)
    # retorna a palvra gerada pela chave
    return code


"""busca a nova letra com base na chave e letra passada"""


def next_char(char: str, key: int) -> str:
    # recupera o index da letra passada para o metódo
    index = alphabet.index(char)
    # busca a posição do index mais o movimento da chave
    pos = index + key
    while pos >= length:
        # enquanto a posição calculada for maior que o tamanho do alfabeto o valor da posição é subtraído pelo tamanho
        # para pegar a posição do novo index caso a chave + index tenha um tamnho maior que o do alfabeto
        pos = pos - length

    return alphabet[pos]


"""decifra a palavra enviada com a chave passada para o método"""


def decipher_word(word: str, key: int) -> str:
    code = ''
    # para cada letra, busca a letra anterior no alfabeto com base na chave
    for char in word:
        code += previous_char(char, key)
    # retorna a palvra gerada pela chave
    return code


def previous_char(char: str, key: int) -> str:
    # recupera o index da letra passada para o metódo
    index = alphabet.index(char)
    # busca a posição do index menos o movimento da chave
    pos = index - key
    while pos < 0:
        # enquanto a posição calculada for menor que 0 o valor do tamanho do alfabeto é adicionado a posição
        # para pegar a posição do novo index caso o index - chave tenha um tamanho menor que 0
        pos = length + pos

    return alphabet[pos]


def brute_force(word: str, hash_set: set) -> (int, str):
    key = 1
    size = len(word)
    while key < 100000:
        print(f"testando chave {key}")
        # descriptografa somente uma palavra
        # para cada valor da chave entre 1 e 100 a palavra é descriptografada usando a chave
        test = ""
        for i in range(size):
            piece = previous_char(word[0 + i: i + 1], key)
            test += piece

        # a palavra é testado contra o dicionário para saber se ela existe de verdade
        if test in hash_set:
            # caso exista a palavra e a chave usada para descriptogravar são retornadas
            return key, test

        key += 1

    # caso ele não ache retorna a ultima chave da tentatica e um erro
    return key, "erro"
