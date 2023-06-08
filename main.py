from battleship.game_configuration import Configuration
from battleship.game import Game


def main() -> None:
    file_path = input('Please enter the path to the configuration file for this game: ')
    game_configuration = Configuration(file_path)
    game_of_battleship = Game(game_configuration)
    game_of_battleship.play()


main()
