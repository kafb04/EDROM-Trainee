def posicaoPonto(x, y, largura, altura):
    centro_x = largura / 2
    centro_y = altura / 2

    if (x == centro_x and y == centro_y):
        pos = "Centro"
    elif (1 <= x <= largura and 1 <= y <= altura):
        pos = ""
        if y < centro_y:
            pos += "Superior "
        elif y > centro_y:
            pos += "Inferior "
        if x < centro_x:
            pos += "Esquerda"
        elif x > centro_x:
            pos += "Direita"
        pos = pos.strip()

        if not ("Superior" in pos or "Inferior" in pos):
            pos = "Centro " + pos.strip()
    else:
        pos = "ERRO: Esta fora dos limites do retangulo!"

    print("A posicao em que o ponto se encontra eh:", pos)

print("Digite o tamanho do retangulo (LarguraxAltura):")
largura, altura = map(int, input().split())

print("Digite as coordenadas do ponto (X,Y):")
x, y = map(int, input().split())

posicaoPonto(x, y, largura, altura)
