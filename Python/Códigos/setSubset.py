T = int(input())

for i in range(T):
    arrA = int(input())
    A = set(map(int, input().split()))
    arrB = int(input())
    B = set(map(int, input().split()))

    subset = A.issubset(B)
    print(subset)