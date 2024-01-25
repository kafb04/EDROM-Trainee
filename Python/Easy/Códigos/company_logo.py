from collections import Counter

def caracteresComuns(s):
    crt = Counter(s)
    comuns = [(char, count) for char, count in crt.items() if count > 0]
    comuns = sorted(comuns, key=lambda x: (-x[1], x[0]))
    return comuns[:3]

if __name__ == '__main__':
    s = input()
    resultado = caracteresComuns(s)
    for caractere, qtd in resultado:
        print(f"{caractere} {qtd}")
