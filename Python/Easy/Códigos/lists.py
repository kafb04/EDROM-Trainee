N = int(input())
lista =[]

for i in range(N):
    op = input().split()

    if op[0] == "insert": lista.insert(int(op[1]),int(op[2]))
    elif op[0] == "append": lista.append(int(op[1]))
    elif op[0] == "pop": lista.pop()
    elif op[0] == "print": print(lista)
    elif op[0] == "remove": lista.remove(int(op[1]))
    elif op[0] == "sort": lista.sort()
    else: lista.reverse()