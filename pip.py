from termcolor import colored
def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-------------")


def take_input(player_token):
    valid = bool
    while valid:
        player_answ = input("Где поставим " + player_token + "?\n")
        try:
            player_answ = int(player_answ)
        except:
            print(colored("Число не обнаружено",'red'))
            continue
        if player_answ >= 1 and player_answ <= 9:
            if (str(board[player_answ - 1]) not in "X0"):
                board[player_answ - 1] = player_token
                valid = False
            else:
                print(colored("Эта клетка уже занята.",'red'))
        else:
            print(colored("Некоректное число.",'red'))


def chek_win(board):
    win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_combination:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False


enumerator = 0
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win = False
while not win:
    draw_board(board)
    if enumerator % 2 == 0:
        take_input(colored("X","magenta"))
    else:
        take_input(colored("0", "blue"))

    enumerator += 1

    if enumerator > 4:
        winner = chek_win(board)
        if winner:
            print(winner, colored("выйграл",'green'))
            win = True
            break
        if enumerator == 9:
            print(colored("Ничья.",'yellow'))
            break
