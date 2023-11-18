import Cifra_de_Cesar


def run():
    print("Lendo dicionário")
    hash_set = get_dicio_data()
    print("Leitura Finalizada")
    while True:
        words = input("digite a palavra ou texto a ser descriptografada\n")
        for word in words.split(" "):
            if not word or not word.isspace():
                print(f"palavra a ser descriptografada {word}")
                resultado = Cifra_de_Cesar.brute_force(word, hash_set)
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
