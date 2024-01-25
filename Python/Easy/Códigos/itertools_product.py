from itertools import product

A = input().split()
B = input().split()

A = [int(elemento) for elemento in A]
B = [int(elemento) for elemento in B]

print(*product(A, B))
