from collections import Counter, OrderedDict

N = int(input())
palavras = Counter()

for _ in range(N):
    lista = input().split()
    palavras.update(lista)

palavras = OrderedDict(palavras)

print(len(palavras))
print(*palavras.values())
