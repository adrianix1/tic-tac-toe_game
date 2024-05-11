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



# TODO 3: input which position player wants to put his mark
# TODO 4: after player puts his mark computer also does it and board is plotted again
# TODO 5: check if computer or player wins
# TODO 6: after the end of game input if player wants to play again
