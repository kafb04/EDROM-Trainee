n = int(input())
arr_ingles = set(map(int, input().split()))
b = int(input())
arr_frances = set(map(int, input().split()))

diferenca = arr_ingles.difference(arr_frances)

print(len(diferenca))