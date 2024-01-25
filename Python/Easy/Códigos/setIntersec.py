n = int(input())
arr_ingles = set(map(int, input().split()))
b = int(input())
arr_frances = set(map(int, input().split()))

intersecao = arr_ingles.intersection(arr_frances)

print(len(intersecao))