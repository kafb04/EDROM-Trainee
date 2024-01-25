n, m = map(int, input().split())
arr = list(map(int, input().split()))
like = set(map(int, input().split()))
dislike = set(map(int, input().split()))

felicidade = 0
for i in arr:
    if i in like:
        felicidade += 1
    elif i in dislike:
        felicidade -= 1
    else:
        felicidade += 0

print(felicidade)
