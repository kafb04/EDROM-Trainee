import numpy

N, M = map(int, input().split())

arr = numpy.array([list(map(float, input().split())) for _ in range(N)])

print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))

std = numpy.std(arr)
std = round(std, 11)
print(std)
