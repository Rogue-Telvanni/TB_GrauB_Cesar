import Cifra_de_Cesar # arquivo com a implementação da difra de cesar


"""ponto de entrado do código"""
def run():
    print("Lendo dicionário")
    hash_set = get_dicio_data()
    print("Leitura Finalizada")
    while True:
        words = input("digite a palavra ou texto a ser descriptografada\n")
        # divide o input do usuário que deve ser um cifra de cesar, caso tenha mais de uma palavra
        # o programa tentara decifrar todas as palavras separadas por espaço
        for word in words.split(" "):
            # caso a palavra seja nula ou espaços brancos ela é ignorada
            if not word or not word.isspace():
                print(f"palavra a ser descriptografada é {word}")
                resultado = Cifra_de_Cesar.brute_force(word, hash_set)
                print(f"Resultado da força bruta: {resultado}")


"""busca os dados do dicionário do alfabeto com palavras sem acentos"""
def get_dicio_data() -> set:
    # cria o hash set para salvar os dados do dicionário
    hash_set = set()
    # abre o arquivo que contem o dicinário que se encontra na mesma pasta do arquivo
    file = open("Dicio.txt", "r")
    # adiciona os valores ao hash set
    for value in file.readlines():
        hash_set.add(value[0: len(value) - 1])

    # fecha o arquivo e retona o hash set
    file.close()
    return hash_set


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
