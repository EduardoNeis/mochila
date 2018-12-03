import random

def geraPopulacaoinicial(tamanhodapop):
    return [geraCromossomo() for x in range (0, tamanhodapop)]


def geraCromossomo():
    return [random.randint(0, 1) for x in range(0, len(ITEMS))]




def main():
    QuantidadeItens = int(input('Insira qual deve ser a quantidade de itens: '))
    TAM_POP = int(input('Insira qual deve ser o tamanho da população: '))
    QTD_ITE = int(input('Insira qual deve ser o numero de iteracoes: '))
    intervalo = int(input('Insira qual deve ser o intervalo de geracoes: '))
    taxa = int(input('Insira qual deve ser a taxa de mutacoes: '))
    CAPACIDADE_MOCHILA = int(input('Insira qual deve ser o peso maximo da mochila: '))
    PESO_OBJ_MAX = int(input('Insira qual deve ser o peso maximo dos objetos: '))
    PESO_OBJ_MIN = int(input('Insira qual deve ser o peso minimo dos objetos '))
    VALOR_OBJ_MAX = int(input('Insira qual deve ser o valor maximo dos objetos: '))
    VALOR_OBJ_MIN = int(input('Insira qual deve ser o valor minimo dos objetos: '))
   geracao = int(1)
   populacao = geraPopulacaoinicial(TAM_POP) #gera nova população


main()