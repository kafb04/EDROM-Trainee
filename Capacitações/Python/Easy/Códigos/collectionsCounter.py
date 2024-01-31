from collections import Counter

X = int(input())
tam_sapato = list(map(int, input().split()))
N = int(input())

tam_disponiveis = Counter(tam_sapato)

total_ganhos = 0

for i in range(N):
    pedido = list(map(int, input().split()))
    tam, preco = pedido[0], pedido[1]

    if tam_disponiveis[tam] > 0:
        total_ganhos += preco
        tam_disponiveis[tam] -= 1

print(total_ganhos)