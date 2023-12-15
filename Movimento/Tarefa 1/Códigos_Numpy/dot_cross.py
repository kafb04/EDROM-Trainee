import numpy

N = int(input())

A = numpy.array([list(map(int, input().split())) for _ in range(N)])
B = numpy.array([list(map(int, input().split())) for _ in range(N)])

dot = numpy.dot(A, B) 
cross = numpy.cross(A, B)

print(dot)
