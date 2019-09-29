import os
import json
from pathlib import PurePath

from window import Window
from menu.game import Game

class Menu(Window):
    """Handles the menu."""

    def __init__(self):
        """Constructor of Menu class."""

        super(Menu, self).__init__()

        self.games = set()
        self.update_games()

    def update_games(self):
        """Updates 'self.games' set with 'info.json' file from games."""

        games_path = PurePath(os.getcwd(), "games/")

        for root, dirs, files in os.walk(games_path):
            for file in files:
                if file == "info.json":
                    with open(PurePath(root, file), "r") as info_json:
                        info = json.loads(info_json.read())

                        name = info["name"]
                        description = info["description"]
                        players = (info["players"]["min"], info["players"]["max"])

                        game = Game(name, description, players)
                        self.games.add(game)
