if __name__ == '__main__':
    estudantes = []
    
    for _ in range(int(input())):
        nome = input()
        nota = float(input())
        estudantes.append((nome, nota))
    
    notasRank = sorted(set(nota for nome, nota in estudantes))[1]
    
    estudantes_notasRank = sorted([nome for nome, nota in estudantes if nota == notasRank])
    
    for estudante in estudantes_notasRank:
        print(estudante)
