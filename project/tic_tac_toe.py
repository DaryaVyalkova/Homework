from random import randint
from os import system
from time import sleep


def draw_board(_board: list) -> None:
    system("cls")

    brd = "============\n||" + \
        _board[0] + "||" + _board[1] + "||" + _board[2] + \
        "||\n============\n||" + \
        _board[3] + "||" + _board[4] + "||" + _board[5] + \
        "||\n============\n||" +  \
        _board[6] + "||" + _board[7] + "||" + _board[8] + \
        "||\n============\n"

    print(brd)


def parse_user_input() -> int:
    while True:
        user_input = input("Введите координату от 1 до 9: ")
        if user_input.isdigit():
            if int(user_input)-1 <= 8 and int(user_input)-1 >= 0:
                return int(user_input)
            else:
                print(
                    f"Такой клетки({user_input}) не существует. Попробуйте еще раз.")
        else:
            print("Введите число от 1 до 9")


def get_player_move(_board: list, _player_type: str):
    while True:
        player_coord = parse_user_input()

        if _board[player_coord-1] in ('X', 'O'):
            print(
                f"Эта клетка({player_coord}) уже занята. Попробуйте еще раз.")
        else:
            _board[player_coord-1] = _player_type
            draw_board(_board)
            return


def get_computer_move(_board: list, _computer_type):
    while True:
        computer_coord = randint(0, 8)
        if _board[computer_coord] not in ('X', 'O'):
            _board[computer_coord] = _computer_type
            draw_board(_board)
            return


def check_free_space(_board: list) -> bool:
    if _board.count(' ') == 0:
        return False
    return True


def check_win(_board: list) -> bool:
    lines = [
        _board[0:3], _board[3:6], _board[6:9],
        _board[0:7:3], _board[1:8:3], _board[2:9:3],
        [_board[0], _board[4], _board[8]],
        [_board[2], _board[4], _board[6]]
    ]

    for line in lines:
        if len(set(line)) == 1 and line[0] != ' ':
            return True
    return False


def main() -> None:
    BOARD = [' ' for i in range(9)]

    while True:
        player_type = input(
            'Введите X или O для выбора (или Q для выхода): ').upper()
        if player_type in ('X', 'O'):
            computer_type = 'O' if player_type == 'X' else 'X'
            break
        elif player_type == 'Q':
            return

    draw_board(BOARD)

    while True:
        if check_free_space(BOARD):
            get_player_move(BOARD, player_type)
            if check_win(BOARD):
                print(f"Победил {player_type}!")
                return
        else:
            break
        sleep(1)
        if check_free_space(BOARD):
            get_computer_move(BOARD, computer_type)
            if check_win(BOARD):
                print(f"Победил {computer_type}!")
                return
        else:
            break

    print("Ничья. Попробуйте еще раз.")


if __name__ == '__main__':
    main()
