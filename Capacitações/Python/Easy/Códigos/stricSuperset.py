arrA = set(map(int, input().split()))
n = int(input())

superset = True

for i in range(n):
    arrN = set(map(int, input().split()))
    if not arrA.issuperset(arrN):
        superset = False
        break

print(superset)
