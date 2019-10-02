import json

class Game:
    """Represents a game.

    Keyword arguments:
    name -- Name of the game
    description -- Description of the game
    version -- Version number of the game
    players -- Minimal and maximal amount of players that can play the game
    """

    def __init__(self, name, description, version, players):
        """Constructor of Game class.

        Keyword arguments:
        name -- Name of the game
        description -- Description of the game
        version -- Version number of the game
        players -- Minimal and maximal amount of players that can play the game
        """

        self.name = name
        self.description = description
        self.version = version
        self.players = players

    def __repr__(self):
        """Representation of Game class."""

        return f"Game({repr(self.name)}, {repr(self.description)}, {repr(self.version)}, {repr(self.players)})"

    def __eq__(self, other):
        """Equality of Game class."""

        if isinstance(other, Game):
            return f"{self.name}{self.version}" == f"{other.name}{other.version}"
        return False

    def __hash__(self):
        """Hash of Game class."""

        return hash(f"{self.name}{self.version}")
