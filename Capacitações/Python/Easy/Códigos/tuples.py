if __name__ == '__main__':
    n = int(input())
    lista = map(int, input().split())
    tupla = tuple(lista)
    t = hash(tupla)
    print(t)
