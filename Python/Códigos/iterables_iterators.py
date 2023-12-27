import itertools

N = int(input())
lista = input().split()
K = int(input())

comb_totais = list(itertools.combinations(range(1, N + 1), K))

comb_A = [comb for comb in comb_totais if any(lista[i - 1] == 'a' for i in comb)]

probabilidade = len(comb_A) / len(comb_totais)

print("{:.3f}".format(probabilidade))
