import numpy

N, M = map(int, input().split())

arr = numpy.array([list(map(int, input().split())) for _ in range(N)])

minimo = numpy.min(arr, axis = 1)
print(numpy.max(minimo))
