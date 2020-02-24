
while True:
    gracz_1 =  str(input('GRACZ 1: wpisz kamień,papier lub nożyce:'))

    gracz_2 = str(input('GRACZ 2: wpisz kamień,papier lub nożyce:'))

    if gracz_1 == gracz_2:
        print("REMIS")


    if gracz_1 == 'kamień' and gracz_2 == 'nożyce':
        print('WYGRAŁ GRACZ 1')
    if gracz_1 == 'nożyce' and gracz_2 == 'papier':
        print('WYGRAŁ GRACZ 1')
    if gracz_1 == 'papier' and gracz_2 == 'kamień':
        print('WYGRAŁ GRACZ 1')

    if gracz_2 == 'kamień' and gracz_1 == 'nożyce':
        print('WYGRAŁ GRACZ 2')
    if gracz_2 == 'nożyce' and gracz_1 == 'papier':
        print('WYGRAŁ GRACZ 2')
    if gracz_2 == 'papier' and gracz_1 == 'kamień':
        print('WYGRAŁ GRACZ 2')

    wyjście = str(input('Chesz zagrać jeszcze raz(Tak/Nie):'))
    if wyjście == 'Tak':
        continue
    else:
        break
