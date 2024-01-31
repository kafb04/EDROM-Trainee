from itertools import permutations

S, k = input().split()
S = sorted(S)
k = int(k)

for perm in permutations(S, k):
    print(''.join(perm))
