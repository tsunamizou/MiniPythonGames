from board import Board

x = int(input("Please enter the side length (5-19) of the board: "))
board = Board(x)
board.print_board()

gameOn = True
while gameOn:
    if board.isGameContinue():
        board.add_piece('🔵')
    else:
        break
    if board.isGameContinue():
        board.add_piece('🔴')
    else:
        break

# ◯ ●