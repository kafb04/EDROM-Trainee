import numpy

arr = input().split()

matriz = numpy.array(arr, dtype=int)
matriz.shape = (3, 3)
print(matriz)      
