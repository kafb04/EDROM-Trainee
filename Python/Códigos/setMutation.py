A = int(input())

listaA = set(map(int, input().split()))

N = int(input())

for i in range(N):
    operation, tam = input().split()
    tam = int(tam)
    arr = set(map(int, input().split()))

    if operation == "intersection_update":
        listaA.intersection_update(arr)
    elif operation == "update":
        listaA.update(arr)
    elif operation == "symmetric_difference_update":
        listaA.symmetric_difference_update(arr)
    elif operation == "difference_update":
        listaA.difference_update(arr)
        
print(sum(listaA))
