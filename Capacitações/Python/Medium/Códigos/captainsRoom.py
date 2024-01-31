K = int(input())
quartos = list(map(int, input().split()))

contador = dict()
for i in quartos:
    contador[i] = contador.get(i, 0) + 1

for i in contador.keys():
    if contador[i] == 1:
        print(i)