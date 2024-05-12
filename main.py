from random import randint
START_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# TODO 1: input which mark player wants to chose


def convert_0(mark):
    if mark == "0":
        mark = "O"
    return mark


def computer_random_move():
    return randint(1, 9)


def update_board(board_in, mark, move=10):
    for el in range(len(board_in)):
        if el == move-1:
            board_in[el] = mark
    board = f"{board_in[0]}|{board_in[1]}|{board_in[2]}\n-+-+-\n" \
            f"{board_in[3]}|{board_in[4]}|{board_in[5]}\n-+-+-\n" \
            f"{board_in[6]}|{board_in[7]}|{board_in[8]}"
    print(board)
    return board_in


player_mark = -1
while player_mark not in ("X", "O"):
    player_mark = input("Provide a valid mark (X, O): ").upper()
    player_mark = convert_0(player_mark)

# TODO 2: print possible positions, 9 digits to chose from
fields_left = START_LIST.copy()
x_and_o_list = START_LIST.copy()
computer_moves = []
player_moves = []

if player_mark == "X":
    computer_mark = "O"
    update_board(x_and_o_list, computer_mark)
else:
    computer_mark = "X"
    computer_move = computer_random_move()
    fields_left.remove(computer_move)
    computer_moves.append(computer_move)
    update_board(x_and_o_list, computer_mark, computer_move)

# TODO 3: input which position player wants to put his mark, check taken positions, keep track of moves in list
player_move = -1
while player_move not in fields_left:
    if player_move == -1:
        pass
    else:
        print("Error. Type a valid number.")
    player_move = int(input('Which field do you want to put your mark? '))
player_moves.append(player_move)
fields_left.remove(player_move)
update_board(x_and_o_list, player_mark, player_move)
# TODO 4: after player puts his mark computer also does it and board is plotted again
# TODO 5: check if computer or player wins, compare with winning combinations
# TODO 6: after the end of game input if player wants to play again
