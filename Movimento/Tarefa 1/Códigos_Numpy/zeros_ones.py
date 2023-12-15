# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

entrada = list(map(int, input().split()))

matriz_zero = numpy.zeros(entrada, dtype = int)
matriz_um = numpy.ones(entrada, dtype = int)

print(matriz_zero)
print(matriz_um)

