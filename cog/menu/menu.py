import pygame
import logging
import os
import json
from pathlib import PurePath, Path

from window import Window
from menu.game import Game

class Menu(Window):
    """Handles the menu."""

    def __init__(self):
        """Constructor of Menu class."""

        super(Menu, self).__init__()

        self.games = set()
        self.update_games()
        logging.debug(self.games)

        self.draw()

    def update_games(self):
        """Updates 'self.games' set with 'info.json' file from games."""

        games_path = PurePath(Path.cwd(), "games/")

        for root, dirs, files in os.walk(games_path):
            for file in files:
                if file == "info.json":
                    with open(PurePath(root, file), "r") as info_json:
                        try:
                            logging.info("Adding a game...")

                            info = json.loads(info_json.read())

                            name = str(info["name"])
                            description = str(info["description"])
                            version = str(info["version"])
                            players = (
                                int(info["players"]["min"]),
                                int(info["players"]["max"])
                            )
                        except ValueError as e:
                            logging.error(
                                f"ValueError: {e}"
                            )
                        except KeyError as e:
                            logging.error(
                                f"KeyError: {e} is not a valid key for 'info'"
                            )
                        else:
                            game = Game(name, description, version, players)
                            self.games.add(game)

                            logging.info("Successfully added a game!")

    def draw(self):
        """Draws the menu."""

        display_info = pygame.display.Info()
        display_width = display_info.current_w
        display_height = display_info.current_h

        # Simulate Display Resolution
        # display_width, display_height = 1920, 400

        self.fill(self.BLACK)

        self.text(
            round(display_width * 0.4375), round(display_height * 0.025),
            "CoG", 120,
            self.WHITE
        )

        self.rect(
            self.YELLOW,
            round(0.05*display_height),
            round(0.05*display_height),
            round(0.3625*display_width),
            display_height - 2*round(0.05*display_height),
            3,
            True)

        for index, game in enumerate(self.games):
            self.text(
                round(1.4*0.05*display_height),
                round(1.4*0.05*display_height + index*0.05*display_height),
                game.name,
                45,
                self.WHITE
            )

            self.text(
                round(0.3625*display_width - 0.4*0.05*display_height),
                round(1.4*0.05*display_height + index*0.05*display_height),
                game.version,
                45,
                self.WHITE
            )
