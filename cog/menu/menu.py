import pygame
import logging
import os
import math
import json
from pathlib import PurePath, Path

from window import Window
from menu.game import Game

class Menu(Window):
    """Handles the menu."""

    def __init__(self):
        """Constructor of Menu class."""

        super(Menu, self).__init__()

        self.games = []
        self.update_games()

        display_info = pygame.display.Info()
        display_width = display_info.current_w
        display_height = display_info.current_h

        # Simulate Display Resolution
        # display_width, display_height = 1920, 400

        self.GAMES_AMOUNT = math.floor(
            (display_height - 2*round(0.05*display_height))                   \
            / (45*display_height/1080)
        )

        self.games_start = 0
        self.selected_game = 0

        self.draw()

    def update_games(self):
        """Updates 'self.games' with 'info.json' file from games."""

        self.games = []

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
                            self.games.append(game)

                            logging.info("Successfully added a game!")

    def pass_event(self, event):
        """Event handler for Main class.

        Keyword arguments:
        event -- Event passed for processing
        """

        if event.level == "host":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.selected_game > 0:
                        self.selected_game -= 1
                    else:
                        pass

                    if self.selected_game - self.games_start < 0:
                        self.games_start -= 1
                    else:
                        pass
                elif event.key == pygame.K_DOWN:
                    if self.selected_game < len(self.games) - 1:
                        self.selected_game += 1
                    else:
                        pass

                    if self.selected_game - self.games_start >= self.GAMES_AMOUNT:# Simulate Display Resolution
        # display_width, display_height = 1920, 400
                        self.games_start += 1
                    else:
                        pass

    def draw(self):
        """Draws the menu."""

        display_info = pygame.display.Info()
        display_width = display_info.current_w
        display_height = display_info.current_h

        # Simulate Display Resolution
        # display_width, display_height = 1920, 400

        self.fill(self.BLACK)

        self.text(
            round(0.4375*display_width), round(0.025*display_height),
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
            True
        )

        shown_games = self.games[self.games_start:self.games_start + self.GAMES_AMOUNT]
        shown_selected_game = self.selected_game - self.games_start

        text_distance = 45*display_height/1080
        text_margin = 1.4*0.05*display_height

        for index, game in enumerate(shown_games):
            if index == shown_selected_game:
                self.text(
                    round(text_margin),
                    round(text_margin + index*text_distance),
                    game.name,
                    45,
                    self.BLACK,
                    background=self.WHITE
                )

                self.text(
                    round(0.3625*display_width - text_margin),
                    round(text_margin + index*text_distance),
                    game.version,
                    45,
                    self.BLACK,
                    background=self.WHITE
                )
            else:
                self.text(
                    round(text_margin),
                    round(text_margin + index*text_distance),
                    game.name,
                    45,
                    self.WHITE
                )

                self.text(
                    round(0.3625*display_width - text_margin),
                    round(text_margin + index*text_distance),
                    game.version,
                    45,
                    self.WHITE
                )
