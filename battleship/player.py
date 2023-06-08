from .board import Board


class Player:
    """
    The player object class
    """
    def __init__(self, number: int):
        self.player_name = input(f'Player {number}, please enter your name: ')
        self.player_firing_board = Board()
        self.player_placement_board = Board()
        self.ship_lengths_sunk = 0

    def create_player(self, game_configuration):
        """
        Creates a new player
        :param game_configuration: The configuration of the game
        :return: A new player with player specific attributes
        """
        self.player_placement_board.create_placement_board(self.player_name, game_configuration)
        self.player_firing_board.create_firing_board(self.player_name, game_configuration)

    def display_game_state(self):
        """
        Displays the current player's current game state
        :return: The current player's firing board and placement board
        """
        print(self.player_firing_board.board_name)
        self.player_firing_board.display_board()
        print(self.player_placement_board.board_name)
        self.player_placement_board.display_board()
