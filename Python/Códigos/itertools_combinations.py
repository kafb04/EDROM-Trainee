from itertools import combinations

S, k = input().split()
S = sorted(S)
k = int(k)

for r in range(1, k + 1):
    for comb in combinations(S, r):
        print(''.join(comb))
