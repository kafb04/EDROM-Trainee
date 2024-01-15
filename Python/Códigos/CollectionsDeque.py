from collections import deque

N = int(input())
d = deque()

for i in range(N):
    operacao = input().split()
    op = operacao[0]

    if op == 'append':
        d.append(int(operacao[1]))
    elif op == 'appendleft':
        d.appendleft(int(operacao[1]))
    elif op == 'pop':
        d.pop()
    elif op == 'popleft':
        d.popleft()

print(*d)
