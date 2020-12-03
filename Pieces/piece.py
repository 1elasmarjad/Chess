import board
import constants


class parent:

    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.alive = True
        self.team = team
        board.gameboard.set_index(x, y, self)


class king(parent):
    pass
    name = "king"

    def __init__(self, x, y, team):
        super().__init__(x, y, team)

    def possible_movements(self):
        return "todo"

    def draw(self):
        print('todo')  # todo


class castle(parent):
    pass
    name = "castle"

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

    def draw(self):
        print('todo')  # todo


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

    def draw(self):
        print('todo')  # todo


class queen(castle, bishop):
    pass
    name = "queen"

    def __init__(self, x, y, team):
        super().__init__(x, y, team)

    def possible_movements(self):
        return self.check_vertical() + self.check_horizontal() + self.check_diagonal()

    def draw(self):
        print('todo')  # todo


class pawn(parent):
    pass
    name = "pawn"

    def __int__(self, x, y, team):
        super().__init__(x, y, team)

    def possible_movements(self):
        possible = []
        if self.team == constants.TEAM_NAME_1:
            if self.y - 1 >= 0 and board.gameboard.peek_index(self.x, self.y - 1).name == "empty":
                possible.append((self.x, self.y - 1))
                if self.y - 2 >= 0 and board.gameboard.peek_index(self.x, self.y - 2).name == "empty":
                    possible.append((self.x, self.y - 2))

        elif self.team == constants.TEAM_NAME_2:
            if self.y + 1 <= 7 and board.gameboard.peek_index(self.x, self.y - 1).name == "empty":
                possible.append((self.x, self.y + 1))
                if self.y + 2 <= 7 and board.gameboard.peek_index(self.x, self.y - 2).name == "empty":
                    possible.append((self.x, self.y + 2))
        return possible

    def draw(self):
        print("Todo")  # todo


class empty:
    name = "empty"
    team = "empty"
