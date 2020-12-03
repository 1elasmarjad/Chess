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
        final_string = ''
        for x in range(len(cls.board_array)):
            for y in range(len(cls.board_array[x])):
                final_string += cls.board_array[x][y].name + ' '
            final_string += '\n'
        return final_string



