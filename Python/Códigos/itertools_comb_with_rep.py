from itertools import combinations_with_replacement 

S, k = input().split()
S = sorted(S)  
k = int(k)

for comb in combinations_with_replacement(S, k):
    print(''.join(comb))