import pygame
import logging
import os
import time
from pathlib import Path, PurePath

os.chdir(Path(__file__).parent)

logging.basicConfig(#filename=PurePath(Path.cwd(), f"logs/{time.strftime('%Y-%m-%d-%H:%M:%S')}.log"),
                    level=logging.DEBUG,
                    format="%(asctime)s::%(levelname)s::%(name)s::%(module)s::%(message)s")

from menu.menu import Menu
from window import Window

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

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    logging.info("Quitting CoG...")
                    running = False

            pygame.display.update()

if __name__ == "__main__":
    Main()
