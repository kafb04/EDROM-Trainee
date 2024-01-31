n = int(input())
arr_ingles = set(map(int, input().split()))
b = int(input())
arr_frances = set(map(int, input().split()))

dif_simetrica = arr_ingles ^ arr_frances

print(len(dif_simetrica))