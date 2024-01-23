n = int(input())
s = set(map(int, input().split()))
Ncomandos = int(input())

for i in range(Ncomandos):
    comando = input().split()
    
    if comando[0] == "remove":
        s.remove(int(comando[1]))
    elif comando[0] == "discard":
        s.discard(int(comando[1]))
    else:
        s.pop()

print(sum(list(s)))
