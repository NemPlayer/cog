import json

class Game:
    """Represents a game.

    Keyword arguments:
    name -- Name of the game
    description -- Description of the game
    version -- Version number of the game
    players -- Min and max amount of players that can play the game
    """

    def __init__(self, name, description, version, players):
        """Constructor of Game class.

        Keyword arguments:
        name -- Name of the game
        description -- Description of the game
        version -- Version number of the game
        players -- Min and max amount of players that can play the game
        """

        self.name = name
        self.description = description
        self.version = version
        self.players = players
