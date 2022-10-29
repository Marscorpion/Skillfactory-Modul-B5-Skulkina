def ruls_of_game():
    print('Добро пожаловать в игру!')
    print('Игрок X и игрок 0 ходят по очереди, первым ходит игрок X')
    print('Введите координаты поля, первая координата - во вертикали, вторая - по горизонтали')


board = [[' '] * 3 for _ in range(3)]


def game_board():
    print(f'    0    1    2')
    for i in range(len(board)):
        print(i, board[i])


def move_in_game():
    def is_valid(move):
        return len(move) == 2 and move[0].isdigit() and move[1].isdigit()

    while True:
        move = input('Введите координаты клетки').split()

        if not is_valid(move):
            print('А может быть все-таки введем два целых числа?')
            continue
        x, y = move
        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Координаты вне диапазона')
            continue
        if board[x][y] == 'x' or board[x][y] == '0':
            print('Клетка занята')
            continue

        return x, y


def check_win():
    win_lines = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                 ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for elem in win_lines:
        line = []
        for c in elem:
            line.append(board[c[0]][c[1]])
            if line == ['x', 'x', 'x']:
                print('Выиглал X, поздравляем!')
                return True
            if line == ['0', '0', '0']:
                print('Выиграл 0, поздравляем!')
                return True
    return False


ruls_of_game()
board = [[' '] * 3 for _ in range(3)]
count_move = 0
while True:
    count_move += 1
    game_board()
    if count_move % 2 == 1:
        print('Ход крестика')
    if count_move % 2 == 0:
        print('Ход нолика')

    x, y = move_in_game()
    if count_move % 2 == 1:
        board[x][y] = 'x'
    if count_move % 2 == 0:
        board[x][y] = 'o'
    if check_win():
        break
    if count_move == 9:
        print('Ничья')
        break



