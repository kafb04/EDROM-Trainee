import numpy

N, M, P = map(int, input().split())

matrizA = numpy.array([list(map(int, input().split())) for _ in range(N)])

matrizB = numpy.array([list(map(int, input().split())) for _ in range(M)])

matrizAB = numpy.concatenate((matrizA, matrizB), axis=0)

print(matrizAB)


