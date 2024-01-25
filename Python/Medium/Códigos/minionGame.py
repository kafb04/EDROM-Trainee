def minion_game(string):
    tam = len(string)
    stuart = 0
    kevin = 0
    for i in range(tam):
        if string[i] not in 'AEIOU':
            stuart += tam - i
        else:
            kevin += tam - i
    if stuart > kevin:
        print(f'Stuart {stuart}')
    elif stuart < kevin:
        print(f'Kevin {kevin}')
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)