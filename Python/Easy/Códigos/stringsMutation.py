def mutate_string(string, pos, character):
    lista = list(string)
    lista[pos] = character
    string = "".join(lista)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)