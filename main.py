from Pieces import piece
import board
import pygame

board.gameboard.start()

board.gameboard.show()

print(board.gameboard.peek_index(0, 1).team)
print(board.gameboard.peek_index(0, 1).name)
print(board.gameboard.peek_index(0, 6).possible_movements())

