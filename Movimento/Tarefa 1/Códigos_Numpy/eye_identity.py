import numpy

numpy.set_printoptions(legacy='1.13')

N, M = map(int, input().split())

matriz_zero = numpy.zeros((N, M), dtype = int)

identidade = numpy.eye(N, M, k = 0)

print(identidade)
