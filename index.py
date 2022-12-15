def hi():
    print('___________________')
    print('  Добро пожаловать')
    print('       в игру     ')
    print('  крестики-нолики ')
    print(' x - номер строки ')
    print(' y - номер столбца')
    print('Значение записываете через пробел')

pole = [[" "]* 3 for i in range(3)]
def show():
    print()
    print('    | 0 | 1 | 2 | ')
    print(' ----------------')
    for i, row in enumerate(pole):
        row_str = f" {i}  | {' | '.join(row)} |"
        print(row_str)
        print(' ----------------')
    print()

def ask():
    while True:
        commands = input('        Ваш ход  ').split()

        if len(commands) != 2:
            print(' Введите 2 координаты! ')
            continue

        x, y = commands

        if not (x.isdigit()) or not (y.isdigit()):
            print(' Введите числа! ')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(' Координаты вне диапазона! ')
            continue

        if pole[x][y] != ' ':
            print(' Клетка занята! ')
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1 ,1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symvols = []
        for c in cord:
            symvols.append(pole[c[0]][c[1]])
            if symvols == ["X","X","X"]:
                print('Выиграл X!!!')
                return True
            if symvols == ["0","0","0"]:
                print('Выиграл 0!!!')
                return True
    return False

hi()
pole = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print('Ходит крестик!')
    else:
        print('Ходит нолик!')

    x, y = ask()

    if count % 2 == 1:
        pole[x][y] = "X"
    else:
        pole[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print('Ничья!')
        break