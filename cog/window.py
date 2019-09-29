import pygame

class Window:
    """Creates a window."""

    def __init__(self):
        """Constructor of Window class."""
        pygame.init()

        self.DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
