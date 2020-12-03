import constants

from Pieces import piece


class gameboard:
    board_array = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ]

    @classmethod
    def make_all_empty(cls):
        EMPTY = piece.empty
        for x in range(len(cls.board_array)):
            for y in range(len(cls.board_array[x])):
                cls.board_array[x][y] = EMPTY

    @classmethod
    def set_index(cls, x, y, as_piece):
        cls.board_array[x][y] = as_piece

    @classmethod
    def peek_index(cls, x, y):
        return cls.board_array[x][y]

    @classmethod
    def is_empty(cls, x, y):
        if cls.board_array[x][y] == piece.empty:
            return True
        return False

    @classmethod
    def has(cls, piece_type):
        """
        :type piece_type: str
        :param: piece_type: the type of piece being searched for
        :returns: True if the type of piece has been found on the board, otherwise returns False
        """

        for x in range(len(cls.board_array)):
            for y in range(len(cls.board_array[x])):
                if cls.board_array[x][y] is not None and cls.board_array[x][y].name == piece_type:
                    return True
        return False

    @classmethod
    def team_has(cls, piece_type, team):
        """
        :type piece_type: str
        :param piece_type: the type of piece being searched for
        :param team: the team that is being searched for (with the piece)
        :return: True if a piece as such has been found, else return False
        """

        for x in range(len(cls.board_array)):
            for y in range(len(cls.board_array[x])):
                if cls.board_array[x][y] is not None and cls.board_array[x][y].name == piece_type and \
                        cls.board_array[x][y].team == team:
                    return True
        return False

    @classmethod
    def show(cls):
        output = ""
        for c in range(len(cls.board_array)):
            for r in range(len(cls.board_array[c])):
                output += cls.board_array[r][c].name + " "
            output += '\n'
        print(output)

    @classmethod
    def start(cls):

        cls.make_all_empty()

        def place(y_major_line, team_name):
            """
            :param y_major_line: the 'y' position (int) of the major line (queen, king, bishop, knight, rook...)
            :param team_name: the name of the team being placed
            """

            piece.rook(0, y_major_line, team_name)
            piece.knight(1, y_major_line, team_name)
            piece.bishop(2, y_major_line, team_name)
            piece.queen(3, y_major_line, team_name)
            piece.king(4, y_major_line, team_name)
            piece.bishop(5, y_major_line, team_name)
            piece.knight(6, y_major_line, team_name)
            piece.rook(7, y_major_line, team_name)

        place(7, constants.TEAM_NAME_1)
        place(0, constants.TEAM_NAME_2)

        #  for in range of board array length
        for x in range(len(gameboard.board_array[0])):
            piece.pawn(x, 1, constants.TEAM_NAME_2)
            piece.pawn(x, 6, constants.TEAM_NAME_1)
