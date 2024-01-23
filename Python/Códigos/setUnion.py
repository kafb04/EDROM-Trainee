n = int(input())
arr_ingles = set(map(int, input().split()))
b = int(input())
arr_frances = set(map(int, input().split()))

uniao = arr_ingles.union(arr_frances)

print(len(uniao))