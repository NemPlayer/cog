import json

class Game:
    """Represents a game.

    Keyword arguments:
    name -- Name of the game
    description -- Description of the game
    players -- Minimal and maximal amount of players that can play the game
    """

    def __init__(self, name, description, players):
        """Constructor of Game class.

        Keyword arguments:
        name -- Name of the game
        description -- Description of the game
        players -- Minimal and maximal amount of players that can play the game
        """

        self.name = name
        self.description = description
        self.players = players

    def __repr__(self):
        """Representation of Game class."""

        return f"Game({repr(self.name)}, {repr(self.description)}, {repr(self.players)})"

    def __eq__(self, other):
        """Equality of Game class."""

        if isinstance(other, Game):
            return self.name == other.name
        return False

    def __hash__(self):
        """Hash of Game class."""

        return hash(self.name)
