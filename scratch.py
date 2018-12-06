import random

# inicializacao de variaveis (tbm para que sejam globais)
QuantidadeItens = 0
TAM_POP = 0
QTD_ITE = 0
intervalo = 0
TAXA_MUTACAO = 0
CAPACIDADE_MOCHILA = 0
PESO_OBJ_MAX = 0
PESO_OBJ_MIN = 0
VALOR_OBJ_MAX = 0
VALOR_OBJ_MIN = 0


class Item(object):
    def __init__(self, v, p):
        self.valor = v
        self.peso = p


def geraPopulacaoinicial(tamanhodapop, qtdItens):
    return [geraCromossomo(qtdItens) for x in range (0, tamanhodapop)]


def geraCromossomo(qtdItens):
    return [random.randint(0, 1) for x in range(0, qtdItens)]


def geraItens():
    ITEMS = [Item(random.randint(VALOR_OBJ_MIN, VALOR_OBJ_MAX), random.randint(PESO_OBJ_MIN, PESO_OBJ_MAX)) for x in range(0, QuantidadeItens)]
    return ITEMS

def main():
    QuantidadeItens = int(input('Insira qual deve ser a quantidade de itens: '))
    TAM_POP = int(input('Insira qual deve ser o tamanho da população: '))
    QTD_ITE = int(input('Insira qual deve ser o numero de iteracoes: '))
    intervalo = int(input('Insira qual deve ser o intervalo de geracoes: '))
    TAXA_MUTACAO = int(input('Insira qual deve ser a taxa de mutacoes: '))
    CAPACIDADE_MOCHILA = int(input('Insira qual deve ser o peso maximo da mochila: '))
    PESO_OBJ_MAX = int(input('Insira qual deve ser o peso maximo dos objetos: '))
    PESO_OBJ_MIN = int(input('Insira qual deve ser o peso minimo dos objetos '))
    VALOR_OBJ_MAX = int(input('Insira qual deve ser o valor maximo dos objetos: '))
    VALOR_OBJ_MIN = int(input('Insira qual deve ser o valor minimo dos objetos: '))
    geracao = 1

    populacao = geraPopulacaoinicial(TAM_POP, QuantidadeItens) #gera nova população
    for g in range(0, QTD_ITE):
        # A linha abaixo organiza a população colocando os individuos com fitness mais alto antes
        populacao = sorted(populacao, key=lambda x: fitness(x), reverse=True)
        for i in populacao:
            print('{} fitness: {}'.format(str(i), fitness(i)))
            populacao = evolutiva(populacao)
            geracao += 1

    print(populacao)

def fitness():
    indice = 0
    for i in target:
        if indice >= QuantidadeItens11:
            break
        if (i == 1):
            valor_total += ITEMS[indice].valor
            peso_total += ITEMS[indice].peso
        indice += 1

    if peso_total > CAPACIDADE_MOCHILA
        return 0 #se o peso total for maior que a capacidade da mochila fitness = 0
    else
        return valor_total


def evolutiva(populacao_):
     tamanhoPais = int(intervalo*TAM_POP)
     pais = populacao_[:tamanhoPais]
     naoPais = populacao_[tamanhoPais:]

    #TODO Roleta dos pais
    for np in naoPais:
        if 0.5 > random.random():
            pais.append(np)


    #TODO Roleta da mutacao
    for
    #TODO Crossover


def mutacao(individuo):
    #TODO funcao de mutacao






main()