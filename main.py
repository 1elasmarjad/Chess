from Pieces import piece
import board

board.gameboard.make_all_empty()

test = piece.pawn(4, 4, "b")

print(test.possible_movements())
