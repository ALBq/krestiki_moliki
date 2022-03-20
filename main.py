def show_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i), *field[i])
def users(f, player,namber):
    while True:
        user_value = input(f'Ход игрока № {namber} играет {player}. Введите координаты:').split()
        if len(user_value) != 2:
            print('Введите два числа...')
            continue
        if not (user_value[0].isdigit() and user_value[1].isdigit()):
            print('Введите числа!')
            continue
        x, y = map(int, user_value)
        if not (x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Уточните координаты!')
            continue
        if f[x][y] != "-":
            print('Клетка занята!')
            continue
        break
    return x, y
def win(f,player):
    win_field = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    for line in win_field:
        win_line = []
        for l in line:
            win_line.append(f[l[0]][l[1]])
        if win_line == [player, player, player]:
            return True
    return False
def begin(field):
    count = 0
    while True:
        show_field(field)
        if count % 2 == 0:
            player = 'x'
            namber = '1'
        else:
            player = 'o'
            namber = '2'
        if count < 9:
            x, y = users(field, player, namber)
            field[x][y] = player
        elif count == 9:
            print('ничья')
            break
        if win(field, player):
            print(f"Выйграл игрок {namber}. Играл {player}")
            print(show_field(field))
            break
        count += 1

field = [['-'] * 3 for _ in range(3)]
begin(field)

