import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for i in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

script_decodificado = ''

for j in range(m):
    for i in range(n):
        script_decodificado += matrix[i][j]

script_decodificado = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', script_decodificado)

print(script_decodificado)
