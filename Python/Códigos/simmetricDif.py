M = int(input())
arrM = set(map(int, input().split()))
N = int(input())
arrN = set(map(int, input().split()))

dif_simetrica = arrM.symmetric_difference(arrN)
sorted_dif_simetrica = sorted(dif_simetrica)

for num in sorted_dif_simetrica:
    print(num)
