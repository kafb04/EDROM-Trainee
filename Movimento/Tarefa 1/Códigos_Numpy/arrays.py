import numpy

def arrays(arr):
    a = numpy.array(arr, float)
    result = numpy.flipud(a)
    return result

arr = input().strip().split(' ')
result = arrays(arr)
print(result)