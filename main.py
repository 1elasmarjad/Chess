from Pieces import piece
import board
import pygame
import constants
import tile


def main():
    def highlight():
        if clicked_piece is not None:
            if clicked_piece.team == GO:
                for positions in clicked_piece.possible_movements():
                    board.gameboard.highlight(positions[0], positions[1], display)
                    tile_highlight = pygame.image.load(constants.SELECTED_EFFECT_PATH)
                    display.blit(tile_highlight, (tile_pos_x, tile_pos_y))
        check_highlight = pygame.image.load(constants.CHECK_EFFECT_PATH)

        if board.gameboard.in_check(constants.TEAM_NAME_1):
            for x in range(len(board.gameboard.board_array)):
                for y in range(len(board.gameboard.board_array[x])):
                    if board.gameboard.board_array[x][y].team == constants.TEAM_NAME_1:
                        display.blit(check_highlight, (x * constants.TILE_SIZE, y * constants.TILE_SIZE))

        elif board.gameboard.in_check(constants.TEAM_NAME_2):
            for x in range(len(board.gameboard.board_array)):
                for y in range(len(board.gameboard.board_array[x])):
                    if board.gameboard.board_array[x][y].team == constants.TEAM_NAME_2:
                        display.blit(check_highlight, (x * constants.TILE_SIZE, y * constants.TILE_SIZE))

    pygame.init()
    pygame.display.set_caption("Chess")
    display = pygame.display.set_mode((1024, 1024))
    clock = pygame.time.Clock()

    board.gameboard.start()  # starts and organizes the chess board

    clicked_piece = None
    tile_pos_x = None
    tile_pos_y = None
    prev_x = None
    prev_y = None
    GO = constants.TEAM_NAME_1  # first go

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
            if pygame.mouse.get_pressed()[0] and board.gameboard.peek_index(grid_x, grid_y).name != "empty" and \
                    board.gameboard.peek_index(grid_x, grid_y).team == GO:
                clicked_piece = board.gameboard.peek_index(grid_x, grid_y)
                tile_pos_x = grid_x * constants.TILE_SIZE
                tile_pos_y = grid_y * constants.TILE_SIZE
                prev_x = grid_x
                prev_y = grid_y

            if prev_x is not None and prev_y is not None and pygame.mouse.get_pressed()[0] and \
                    (grid_x, grid_y) in board.gameboard.peek_index(prev_x, prev_y).possible_movements() and \
                    board.gameboard.peek_index(prev_x, prev_y).team == GO:

                pc = board.gameboard.peek_index(prev_x, prev_y)

                board.gameboard.move_to(pc, grid_x, grid_y)
                if GO == constants.TEAM_NAME_1:
                    GO = constants.TEAM_NAME_2
                else:
                    GO = constants.TEAM_NAME_1
                prev_x = None
                prev_y = None

                # board.gameboard.show()  #DEBUG

        highlight()  # highlight hovering
        board.gameboard.draw_pieces(display)  # draws all the game pieces
        pygame.display.update()

        # CHECK FOR WINNER:

        if not board.gameboard.team_has('king', constants.TEAM_NAME_1):
            running = False
            return constants.TEAM_NAME_2
        elif not board.gameboard.team_has('king', constants.TEAM_NAME_2):
            running = False
            return constants.TEAM_NAME_1

        clock.tick(constants.FRAME_RATE)


constants.TEAM_NAME_1 = 'Team white'
constants.TEAM_NAME_2 = 'Team black'

if main() == constants.TEAM_NAME_1:
    print(f"{constants.TEAM_NAME_1} wins!")
else:
    print(f"{constants.TEAM_NAME_2} wins!")
