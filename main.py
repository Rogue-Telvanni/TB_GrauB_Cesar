import Cifra_de_Cesar


def run():
    print("Lendo dicionário")
    hash_set = get_dicio_data()
    print("Leitura Finalizada")
    while True:
        words = input("digite a palavra ou texto a ser criptografada, sera usado força bruta para tentar descriptografala\n")
        chave = int(input("digite a chave, ela deve ser um numero\n"))
        for word in words.split(" "):
            if not word or not word.isspace():
                print(f"palavra teste {word}")
                cipher = Cifra_de_Cesar.cipher_word(word, chave)
                print(f"cifra gerada: {cipher}")
                resultado = Cifra_de_Cesar.brute_force(cipher, hash_set)
                print(f"Resultado da força bruta: {resultado}")


def get_dicio_data() -> set:
    hash_set = set()
    file = open("Dicio.txt", "r")
    for value in file.readlines():
        hash_set.add(value[0: len(value) - 1])

    file.close()
    return hash_set


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
