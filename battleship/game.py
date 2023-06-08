from .player import Player


class Game:
    """
    The game object, sets up and plays the game
    """
    def __init__(self, game_configuration):
        self.game_config = game_configuration
        self.total_ship_lengths = game_configuration.total_ship_lengths
        self.player_1 = Player(1)
        self.player_2 = Player(2)
        self.turns = 0
        self.current_player = self.player_1
        self.other_player = self.player_2
        self.player_list = [self.player_1, self.player_2]

    def get_cur_player(self) -> object:
        """
        Gets the current player
        :return: The current player making a move
        """
        if self.turns % 2 == 0:
            self.current_player = self.player_1
            return self.current_player
        else:
            self.current_player = self.player_2
            return self.current_player

    def get_other_player(self) -> object:
        """
        Gets the other defending player
        :return: The defending other player
        """
        if self.turns % 2 == 0:
            self.other_player = self.player_2
            return self.other_player
        else:
            self.other_player = self.player_1
            return self.other_player

    def switch_to_next_player(self) -> None:
        """
        Helps with the switching of current player
        :return: A +1 to the turns in the game
        """
        self.turns += 1

    def play(self) -> None:
        """
        The play function
        :return: An announcment of the results of the game
        """
        self.player_1.create_player(self.game_config)
        self.player_2.create_player(self.game_config)
        while not self.is_over():
            self.current_player = self.get_cur_player()
            self.other_player = self.get_other_player()
            self.take_turn()
            self.switch_to_next_player()
        self.announce_results()

    def is_over(self) -> bool:
        """
        Determines if the game is over or not
        :return: A boolean value on if the game is over or not
        """
        for player in self.player_list:
            if self.total_ship_lengths == player.ship_lengths_sunk:
                return True
        return False

    def announce_results(self):
        """
        Announces the results of the game
        :return: Displays the game state and the winner
        """
        winning_player = self.player_list[0]
        for player in self.player_list:
            if player.ship_lengths_sunk > winning_player.ship_lengths_sunk:
                winning_player = player
        winning_player.display_game_state()
        print(f"{winning_player.player_name} won!")

    def take_turn(self) -> None:
        """
        Gets and executes the current player's attack
        :return:
        """
        self.current_player.display_game_state()
        attack = self.get_move()
        self.do(attack)

    def get_move(self) -> list:
        """
        Gets the current player's move
        :return: A list containing the current player's row and col attack
        """
        prompt = f'{self.current_player.player_name}, enter the location you want to fire at in the form row col: '
        attack = input(prompt)
        while not self.valid_input(attack):
            attack = input(prompt)
        return attack.split()

    def valid_input(self, attack) -> bool:
        """
        Determines if the current player's attack is valid
        :param attack: The inputted attack
        :return:A boolean value on if the attack is valid or not
        """
        if len(attack.split()) == 2:
            row, col = attack.split()
            if row.isdigit() and col.isdigit():
                if (int(row) <= self.current_player.player_firing_board.board_rows - 1) and (int(col) <= self.current_player.player_firing_board.board_cols - 1):
                    if self.current_player.player_firing_board.board[int(row)][int(col)] == '*':
                        return True
        else:
            return False

    def do(self, attack: list):
        """
        Executes the attack
        :param attack: The given attack by the current player
        :return:
        """
        row, col = attack
        if self.hit(int(row), int(col), self.other_player.player_placement_board.board):
            ship = self.other_player.player_placement_board.board[int(row)][int(col)]
            print(f"{self.current_player.player_name} hit {self.other_player.player_name}'s {ship}!")
            self.other_player.player_placement_board.board[int(row)][int(col)] = 'X'
            self.current_player.player_firing_board.board[int(row)][int(col)] = 'X'
            self.current_player.ship_lengths_sunk += 1
            num_ship = 0
            for board_row in self.other_player.player_placement_board.board:
                for board_column in board_row:
                    if ship == board_column:
                        num_ship += 1
            if num_ship == 0:
                print(f"{self.current_player.player_name} destroyed {self.other_player.player_name}'s {ship}!")
        else:
            print(f"{self.current_player.player_name} missed.")
            self.other_player.player_placement_board.board[int(row)][int(col)] = 'O'
            self.current_player.player_firing_board.board[int(row)][int(col)] = 'O'
        return

    def hit(self, row: int, col: int, other_player_placement_board) -> bool:
        """
        Determines if the attack has hit or not
        :param row: The row value of the attack
        :param col: The column value of the attack
        :param other_player_placement_board: The other player's placement board
        :return: Whether or not the attack hit
        """
        if other_player_placement_board[row][col] != '*':
            return True
        else:
            return False

