from collections import OrderedDict

N = int(input())
dicionario = OrderedDict()

for i in range(N):
    item = input().split()
    nome, preco = " ".join(item[:-1]), int(item[-1])  
    if nome in dicionario:
        dicionario[nome] += preco
    else:
        dicionario[nome] = preco

for nome, preco in dicionario.items():
    print(f'{nome} {preco}')
