QuantidadeItens = int(input('Insira a quantidade de itens: '))
x=0
PesoItem = []
ValorItem = []
while x < QuantidadeItens:
    PesoItem.append(int(input('Insira o peso do item: ')))
    ValorItem.append(int(input('Insira o valor do item: ')))
    x +=1

print(PesoItem)
print(ValorItem)