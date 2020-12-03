import board
import constants
import pygame


class parent:

    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.alive = True
        self.team = team
        board.gameboard.set_index(x, y, self)

    def kill(self):
        self.alive = False


# ----------KING----------

class king(parent):
    pass
    name = "king"
    check_mate = False
    stuck = False

    def __init__(self, x, y, team):
        super().__init__(x, y, team)

    def possible_movements(self):
        possible = []

        def viable(final_x, final_y, player_team):
            if 0 <= final_x <= 7 and 0 <= final_y <= 7 \
                    and board.gameboard.peek_index(final_x, final_y).team != player_team:
                return True
            return False

        # UP, DOWN, LEFT, RIGHT
        if viable(self.x, self.y + 1, self.team):
            possible.append((self.x, self.y + 1))
        if viable(self.x, self.y - 1, self.team):
            possible.append((self.x, self.y - 1))
        if viable(self.x + 1, self.y, self.team):
            possible.append((self.x + 1, self.y))
        if viable(self.x - 1, self.y, self.team):
            possible.append((self.x - 1, self.y))

        # CORNERS
        if viable(self.x - 1, self.y - 1, self.team):
            possible.append((self.x - 1, self.y - 1))
        if viable(self.x - 1, self.y + 1, self.team):
            possible.append((self.x - 1, self.y + 1))
        if viable(self.x + 1, self.y - 1, self.team):
            possible.append((self.x + 1, self.y - 1))
        if viable(self.x + 1, self.y + 1, self.team):
            possible.append((self.x + 1, self.y + 1))

        return possible

    def draw(self, display):
        pass  # todo


# ----------ROOK----------

class rook(parent):
    pass
    name = "rook"

    def __init__(self, x, y, team):
        super().__init__(x, y, team)

    def possible_movements(self):
        return self.check_horizontal() + self.check_vertical()

    def check_horizontal(self):
        possible = []

        # LEFT:
        search_xloc = self.x - 1  # the position in which the search will begin
        while search_xloc >= 0 and board.gameboard.peek_index(search_xloc, self.y).team != self.team:

            if board.gameboard.peek_index(search_xloc, self.y).team != "empty" and \
                    board.gameboard.peek_index(search_xloc, self.y).team != self.team:
                # in the case that the search position is an opponent...
                possible.append((search_xloc, self.y))
                break

            possible.append((search_xloc, self.y))
            search_xloc -= 1

            # RIGHT:
        search_xloc = self.x + 1  # the position in which the search will begin
        while search_xloc <= 7 and board.gameboard.peek_index(search_xloc, self.y).team != self.team:

            if board.gameboard.peek_index(search_xloc, self.y).team != "empty" and \
                    board.gameboard.peek_index(search_xloc, self.y).team != self.team:
                # in the case that the search position is an opponent...
                possible.append((search_xloc, self.y))
                break

            possible.append((search_xloc, self.y))
            search_xloc += 1

        return possible

    def check_vertical(self):
        possible = []

        # UPWARDS:
        search_yloc = self.y - 1  # the position in which the search will begin
        while search_yloc >= 0 and board.gameboard.peek_index(self.x, search_yloc).team != self.team:

            if board.gameboard.peek_index(self.x, search_yloc).team != "empty" and \
                    board.gameboard.peek_index(self.x, search_yloc).team != self.team:
                # in the case that the search position is an opponent...
                possible.append((self.x, search_yloc))
                break

            possible.append((self.x, search_yloc))
            search_yloc -= 1

        search_yloc = self.y + 1  # the position in which the search will begin
        while search_yloc <= 7 and board.gameboard.peek_index(self.x, search_yloc).team != self.team:

            if board.gameboard.peek_index(self.x, search_yloc).team != "empty" and \
                    board.gameboard.peek_index(self.x, search_yloc).team != self.team:
                # in the case that the search position is an opponent...
                possible.append((self.x, search_yloc))
                break

            possible.append((self.x, search_yloc))
            search_yloc += 1

        return possible

    def draw(self, display):
        pass  # todo


# ----------BISHOP----------

class bishop(parent):
    pass
    name = "bishop"

    def __int__(self, x, y, team):
        super().__init__(x, y, team)

    def possible_movements(self):
        return self.check_diagonal()

    def check_diagonal(self):
        possible = []

        # TOP LEFT:
        search_xloc = self.x - 1
        search_yloc = self.y - 1

        while search_yloc >= 0 and search_xloc >= 0 and \
                board.gameboard.peek_index(search_xloc, search_yloc).team != self.team:

            if board.gameboard.peek_index(search_xloc, search_yloc).team != "empty" and \
                    board.gameboard.peek_index(search_xloc, search_yloc).team != self.team:
                # in the case that the search position is an opponent...
                possible.append((search_xloc, search_yloc))
                break

            possible.append((search_xloc, search_yloc))
            search_xloc -= 1
            search_yloc -= 1

        # TOP RIGHT:
        search_xloc = self.x + 1
        search_yloc = self.y - 1

        while search_yloc >= 0 and search_xloc <= 7 and \
                board.gameboard.peek_index(search_xloc, search_yloc).team != self.team:

            if board.gameboard.peek_index(search_xloc, search_yloc).team != "empty" and \
                    board.gameboard.peek_index(search_xloc, search_yloc).team != self.team:
                # in the case that the search position is an opponent...
                possible.append((search_xloc, search_yloc))
                break

            possible.append((search_xloc, search_yloc))
            search_xloc += 1
            search_yloc -= 1

        # BOTTOM LEFT:
        search_xloc = self.x - 1
        search_yloc = self.y + 1

        while search_yloc <= 7 and search_xloc >= 0 and \
                board.gameboard.peek_index(search_xloc, search_yloc).team != self.team:

            if board.gameboard.peek_index(search_xloc, search_yloc).team != "empty" and \
                    board.gameboard.peek_index(search_xloc, search_yloc).team != self.team:
                # in the case that the search position is an opponent...
                possible.append((search_xloc, search_yloc))
                break

            possible.append((search_xloc, search_yloc))
            search_xloc -= 1  # move search position to the left
            search_yloc += 1  # move search position to the left

        # BOTTOM RIGHT:
        search_xloc = self.x + 1
        search_yloc = self.y + 1

        while search_yloc <= 7 and search_xloc <= 7 and \
                board.gameboard.peek_index(search_xloc, search_yloc).team != self.team:

            if board.gameboard.peek_index(search_xloc, search_yloc).team != "empty" and \
                    board.gameboard.peek_index(search_xloc, search_yloc).team != self.team:
                # in the case that the search position is an opponent...
                possible.append((search_xloc, search_yloc))
                break

            possible.append((search_xloc, search_yloc))
            search_xloc += 1  # move search position to the left
            search_yloc += 1  # move search position to the left
        return possible

    def draw(self, display):
        pass  # todo


# ----------KNIGHT----------

class knight(parent):
    pass
    name = "knight"

    def possible_movements(self):
        possible = []

        def viable(pos_x, pos_y, player_team):
            if 0 <= pos_x <= 7 and 0 <= pos_y <= 7 \
                    and board.gameboard.peek_index(pos_x, pos_y).team != player_team:
                return True
            return False

        if viable(self.x - 1, self.y + 2, self.team):
            possible.append((self.x - 1, self.y + 2))

        if viable(self.x + 1, self.y + 2, self.team):
            possible.append((self.x + 1, self.y + 2))

        if viable(self.x - 2, self.y + 1, self.team):
            possible.append((self.x - 2, self.y + 1))

        if viable(self.x - 1, self.y - 2, self.team):
            possible.append((self.x - 1, self.y - 2))

        if viable(self.x + 1, self.y - 2, self.team):
            possible.append((self.x + 1, self.y - 2))

        if viable(self.x + 2, self.y - 1, self.team):
            possible.append((self.x + 2, self.y - 1))

        if viable(self.x - 2, self.y - 1, self.team):
            possible.append((self.x - 2, self.y - 1))

        return possible

    def draw(self, display):
        pass  # todo


# ----------QUEEN----------

class queen(rook, bishop):
    pass
    name = "queen"

    def __init__(self, x, y, team):
        super().__init__(x, y, team)

    def possible_movements(self):
        return self.check_vertical() + self.check_horizontal() + self.check_diagonal()

    def draw(self, display):
        pass  # todo


# ----------PAWN----------

class pawn(parent):
    pass
    name = "pawn"
    moved_once = False

    def __int__(self, x, y, team):
        super().__init__(x, y, team)

    def possible_movements(self):
        possible = []
        if self.team == constants.TEAM_NAME_1:
            if self.y - 1 >= 0 and board.gameboard.peek_index(self.x, self.y - 1).name == "empty":
                possible.append((self.x, self.y - 1))
                if not self.moved_once and self.y - 2 >= 0 and board.gameboard.peek_index(self.x,
                                                                                          self.y - 2).name == "empty":
                    possible.append((self.x, self.y - 2))

            if board.gameboard.peek_index(self.x - 1, self.y - 1) is not None and \
                    board.gameboard.peek_index(self.x - 1, self.y - 1).name == constants.TEAM_NAME_2:
                possible.append((self.x - 1, self.y - 1))

            if self.x + 1 <= 7 and self.y - 1 >= 0 and \
                    board.gameboard.peek_index(self.x + 1, self.y - 1).name == constants.TEAM_NAME_2:
                possible.append((self.x + 1, self.y - 1))

        elif self.team == constants.TEAM_NAME_2:
            if self.y + 1 <= 7 and board.gameboard.peek_index(self.x, self.y + 1).team == "empty":
                possible.append((self.x, self.y + 1))
                if not self.moved_once and self.y + 2 <= 7 and \
                        board.gameboard.peek_index(self.x, self.y + 2).team == "empty":
                    possible.append((self.x, self.y + 2))

            if board.gameboard.peek_index(self.x - 1, self.y + 1) is not None and \
                    board.gameboard.peek_index(self.x - 1, self.y + 1).team == constants.TEAM_NAME_1:
                possible.append((self.x - 1, self.y + 1))

            if self.x + 1 <= 7 and self.y + 1 <= 7 and \
                    board.gameboard.peek_index(self.x + 1, self.y + 1).team == constants.TEAM_NAME_1:
                possible.append((self.x + 1, self.y + 1))

        return possible

    def draw(self, display):
        if self.team == constants.TEAM_NAME_2:
            img = pygame.image.load(constants.TEAM_2_PAWN_PATH)
            display.blit(img, (self.x * constants.TILE_SIZE, self.y * constants.TILE_SIZE))


# ----------EMPTY----------

class empty:
    name = "empty"
    team = "empty"
