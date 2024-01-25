from collections import deque

def empilhar_blocos(num_casos, casos):
    resultados = []
    for n, blocos in casos:
        fila = deque(blocos)
        topo = float('inf')
        for i in range(n):
            if fila[0] >= fila[-1] and fila[0] <= topo: topo = fila.popleft()
            elif fila[-1] <= topo: topo = fila.pop()
            else:
                resultados.append("No")
                break
        else: resultados.append("Yes")
    return resultados

num_casos = int(input())
casos = [(int(input()), list(map(int, input().split()))) for _ in range(num_casos)]
resultados = empilhar_blocos(num_casos, casos)
print(*resultados, sep="\n")
