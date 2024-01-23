import calendar

d = list(map(int, input().split()))

if len(d) == 3:
    mes, dia, ano = d
    if 1 <= mes <= 12 and 1 <= dia <= calendar.monthrange(ano, mes)[1]:
        dia_semana = calendar.weekday(ano, mes, dia)
        dia_nome = calendar.day_name[dia_semana]
        print(dia_nome.upper())
    else:
        print()
else:
    print()
