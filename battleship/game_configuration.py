class Configuration:
    """
    The configuration for the game
    """
    def __init__(self, file):
        self.total_ship_lengths = 0
        self.ship_info = []
        with open(file, 'r') as f:
            line = f.readline()
            self.rows = line.strip()
            line = f.readline()
            self.col = line.strip()
            line = f.readline()
            self.num_ships = line.strip()
            for line in f:
                ship_name, length = line.split()
                self.total_ship_lengths += int(length)
                self.ship_info.append([ship_name, length])
            self.ship_info.sort()