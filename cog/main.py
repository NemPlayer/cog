import pygame
import logging
import os
import time
from pathlib import Path, PurePath

os.chdir(Path(__file__).parent)

logging.basicConfig(
    filename=PurePath(Path.cwd(), f"logs/{time.strftime('%Y-%m-%d %X')}.log"),
    level=logging.DEBUG,
    format="%(asctime)s::%(levelname)s::%(name)s::%(module)s::%(message)s"
)

from events import Events
from menu.menu import Menu

class Main:
    """Entry point for CoG."""

    def __init__(self):
        """Constructor of Main class."""

        pygame.init()

        self.window = Menu()

        self.run()

    def run(self):
        """Runs CoG."""

        running = True

        events = Events()

        while running:
            for event in events:
                self.window.pass_event(event)

                if event.level == "host":
                    if event.type == pygame.KEYDOWN:
                        if event.mod & pygame.KMOD_CTRL:
                            if event.key == pygame.K_ESCAPE:
                                running = False

            self.window.draw()
            pygame.display.update()


if __name__ == "__main__":
    Main()
