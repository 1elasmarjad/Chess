from Pieces import piece
import board
import pygame

FRAME_RATE = 30

pygame.init()
pygame.display.set_caption("Chess")
display = pygame.display.set_mode((1024, 1024))
clock = pygame.time.Clock()

running = True

board.gameboard.start()  # starts and organizes the chess board

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # breaks out of running loop

    board.gameboard.draw()

    pygame.display.update()
    clock.tick(FRAME_RATE)
