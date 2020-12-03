from Pieces import piece
import board
import pygame
import constants
import tile


def main():
    pygame.init()
    pygame.display.set_caption("Chess")
    display = pygame.display.set_mode((1024, 1024))
    clock = pygame.time.Clock()

    board.gameboard.start()  # starts and organizes the chess board

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # breaks out of running loop

        mouse_x, mouse_y = pygame.mouse.get_pos()  # mouse positions

        board.gameboard.draw_background(display)  # draws the checker background

        if tile.controller.in_a_tile(mouse_x, mouse_y):  # checks if cursor is in a tile
            hovering_tile = tile.controller.in_a_tile(mouse_x, mouse_y)  # the tile the client is hovering above
            hovering_tile.hover_effect(display)  # turn on the hover effect on the position the cursor is

            grid_x, grid_y = hovering_tile.grid_pos()  # the x and y locations of the cursor in terms of the grid
            if pygame.mouse.get_pressed()[0] and board.gameboard.peek_index(grid_x, grid_y) != piece.empty:
                clicked_piece = board.gameboard.peek_index(grid_x, grid_y)
                for positions in clicked_piece.possible_movements():
                    board.gameboard.highlight(positions[0], positions[1], display)

        board.gameboard.draw_pieces(display)  # draws all the game pieces
        pygame.display.update()
        clock.tick(constants.FRAME_RATE)


main()
