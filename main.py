from random import randint
START_BOARD = "1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9"

# TODO 1: input which mark player wants to chose


def convert_0(mark):
    if mark == "0":
        mark = "O"
    return mark


player_mark = -1
while player_mark not in ("X", "O"):
    player_mark = input("Provide a valid mark (X, O): ").upper()
    player_mark = convert_0(player_mark)

# TODO 2: print positions possible, 9 digits to chose from
if player_mark == "X":
    computer_mark = "O"
    print(START_BOARD)
else:
    computer_mark = "X"
    computer_move = str(randint(1, 9))
    board = START_BOARD
    board = board.replace(computer_move, computer_mark)
    print(board)

# TODO 3: input which position player wants to put his mark, check taken positions, keep track of moves in list
# TODO 4: after player puts his mark computer also does it and board is plotted again
# TODO 5: check if computer or player wins, compare with winning combinations
# TODO 6: after the end of game input if player wants to play again
