class Board:
    """
    The board object class for each player's firing board and placement board
    """
    def __init__(self):
        self.board_name = ''
        self.board_rows = 0
        self.board_cols = 0
        self.board = []

    def make_empty_board(self):
        """
        Makes an empty board based on the game configurations
        :return: An empty board based on the game configurations
        """
        board = []
        for row_num in range(self.board_rows):
            row = []
            for col_num in range(self.board_cols):
                row.append('*')
            board.append(row)
        return board

    def create_firing_board(self, player_name: str, configuration):
        """
        Creates a firing board
        :param player_name: The player's name who the board is being made for
        :param configuration: The configuration of the game
        :return: A firing board for the player
        """
        self.board_rows = int(configuration.rows)
        self.board_cols = int(configuration.col)
        self.board_name = f"{player_name}'s Firing Board"
        self.board = self.make_empty_board()
        return self.board

    def create_placement_board(self, player_name: str, configuration):
        """
        Creates a placement board
        :param player_name: The name of the player who the board is being made for
        :param configuration: The configuration of the game
        :return: A placement board for a player
        """
        self.board_rows = int(configuration.rows)
        self.board_cols = int(configuration.col)
        self.board_name = f"{player_name}'s Placement Board"
        self.board = self.make_empty_board()
        print(self.board_name)
        self.display_board()
        for ship_name, length in configuration.ship_info:
            orientation, position = self.get_ship_placement(player_name, ship_name, int(length))
            row, col = position
            if orientation[0] == ('v' or 'V'):
                for i in range(int(length)):
                    self.board[int(row) + i][int(col)] = ship_name
            else:
                for i in range(int(length)):
                    self.board[int(row)][int(col) + i] = ship_name
            print(self.board_name)
            self.display_board()
        return self.board

    def display_board(self):
        """
        Displays either a placement or firing board
        :return: A player's placement or firing board
        """
        print(end=' ')
        for i in range(len(list(zip(*self.board)))):  # column headers
            print(f' {i}', end = '')
        print()  # printing board
        for row_index in range(self.board_rows):  # row headers
            print(row_index , ' '.join(self.board[row_index]))

    def get_ship_placement(self, name: str, ship_name: str, length: int):
        """
        Gets the current player's desired ship placement
        :param name: The current player's name
        :param ship_name: The name of the ship
        :param length: The length of the ship
        :return: The desired placement of the ship
        """
        orientation = 'f'
        while not self.valid_orientation(orientation):
            orientation = input(f'{name}, enter the orientation of your {ship_name}, which is {length} long: ')
            orientation = orientation.strip().lower()
            if self.valid_orientation(orientation):
                position = input(f'Enter the starting location for your {ship_name}, which is {length}'
                                 f' long, in the form row col: ')
                if not self.valid_placement(position, orientation, length):
                    orientation = 'f'
                else:
                    return orientation, position.split()

    def valid_orientation(self, orientation: str) -> bool:
        """
        Determines if the orientation of the ship is a valid orientation
        :param orientation: The given orientation
        :return: A boolean value on if the orientation is valid
        """
        valid_input = ['v', 've', 'ver', 'vert', 'verti', 'vertic', 'vertica', 'vertical', 'vertically',
                       'h', 'ho', 'hor', 'hori', 'horiz', 'horizo', 'horizon', 'horizont', 'horizonta', 'horizontal',
                       'horizontally']
        if orientation in valid_input:
            return True
        else:
            return False

    def valid_placement(self, position, orientation, length: int) -> bool:
        """
        Determines if the player's desired placement of the ship is valid
        :param position: The desired position to place the ship
        :param orientation: The desired orientation of the ship
        :param length: The length of the ship
        :return: Whether or not if the placement is valid
        """
        if len(position.split()) == 2:
            row, col = position.split()
            if row.isdigit() and col.isdigit():
                if self.within_range(orientation, int(row), int(col),
                                     int(length)) and self.is_empty(orientation, int(row), int(col), int(length)):
                    return True
        else:
            return False

    def within_range(self, orientation: str, row: int, col: int, length: int) -> bool:
        """
        Determines if the placement of the ship is within range of the board
        :param orientation: The orientation of the ship
        :param row: The row value of placement for the ship
        :param col: The column value of placement for the ship
        :param length: The length of the ship
        :return: If the desired ship placement is wihtin range of the board
        """
        verticals = ['v', 've', 'ver', 'vert', 'verti', 'vertic', 'vertica', 'vertical', 'vertically']
        horizontals = ['h', 'ho', 'hor', 'hori', 'horiz', 'horizo', 'horizon', 'horizont', 'horizonta', 'horizontal',
                       'horizontally']
        if orientation.lower() in verticals:
            if ((int(row) + int(length)) <= self.board_rows) and (int(col) <= self.board_cols - 1):
                return True
        elif orientation in horizontals:
            if ((int(col) + int(length)) <= self.board_cols) and (int(row) <= self.board_rows):
                return True

    def is_empty(self, orientation: str, row: int, col: int, length: int):
        """
        Determines if there are empty spaces for a ship to be placed at desired location
        :param orientation: The desired orientation of the ship
        :param row: The row value of the desired placement
        :param col: The column value of the desired placement
        :param length: The length of the ship
        :return: If spaces are empty or not
        """
        if orientation[0] == ('v' or 'V'):
            for i in range(length):
                if self.board[row + i][col] != '*':
                    return False
            return True
        elif orientation[0] == ('h' or 'H'):
            for i in range(length):
                if self.board[row][col + i] != '*':
                    return False
            return True




