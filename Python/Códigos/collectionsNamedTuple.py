from collections import namedtuple

N = int(input())

colunas = input().split()

Estudante = namedtuple('Estudante', colunas)

total_notas = 0

for i in range(N):
    info = input().split()
    estudante = Estudante(*info)
    notas = float(estudante.MARKS)
    total_notas += notas

media_notas = total_notas / N

print("{:.2f}".format(media_notas))
