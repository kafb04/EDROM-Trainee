import numpy

N = int(input())

A = numpy.array([list(map(float, input().split())) for _ in range(N)])

determinante = numpy.linalg.det(A)
print(round(determinante, 2))
