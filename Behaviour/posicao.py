# TAREFA 1 - BEHAVIOUR

def posicaoPonto(x, y):
    if (10 >= x >= 0 and 10 >= y >= 0) :
        pos = "Superior Direita"

    elif (10 >= x >= 0 and 0 >= y >= -10) :
        pos = "Inferior Direita"

    elif (0 >= x >= -10 and 10 >= y >= 0) :
        pos = "Superior Esquerda"

    elif (0 >= x >= -10 and 0 >= y >= -10) :
        pos = "Inferior Direita"

    elif (x == 0 and y == 0) :
        pos = "Centro"

    else:
        pos = "ERRO: As coordenadas se encontram fora do plano cartesiano, cujo limite é 10x10!"
    
    print("A posicao em que o ponto se encontra eh:", pos)


print("Digite as coordenadas (X, Y)")
x = int(input())
y = int(input())
posicaoPonto(x, y)
