import pygame
import os
from pathlib import Path

os.chdir(Path(__file__).parent)

from menu.menu import Menu
from window import Window

class Main:
    """Entry point for CoG."""

    def __init__(self):
        """Constructor of Main class."""

        self.window = Menu()

        self.run()

    def run(self):
        """Runs CoG."""

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    running = False

            pygame.display.update()

if __name__ == "__main__":
    Main()
