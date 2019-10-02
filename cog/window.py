import pygame
import math
import logging
from pathlib import PurePath

from fonts.fonts import FONTS as MAIN_FONTS

class Window:
    """Creates a window."""

    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)

    def __init__(self):
        """Constructor of Window class."""

        self.DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def fill(self, color, rect=None, special_flags=0):
        """Fill 'DISPLAYSURF' with a solid color.

        Keyword arguments:
        color -- Color with which 'DISPLAYSURF' is filled
        rect -- If given, limits the fill of 'DISPLAYSURF' to a specific area
        special_flag -- If given, controls the use of colors
        """

        self.DISPLAYSURF.fill(color, rect, special_flags)

    def rect(self, color, left, top, width, height, thickness=1, rounded=False):
        """Draw a rectangle.

        Keyword arguments:
        color -- Color to draw with
        left -- x-coordinate (left-most is 0)
        top -- y-coordtinate (top-most is 0)
        width -- Width of the rect
        height -- Height of the rect
        thickness -- Used for line thickness
        rounded -- If True, the rectangle has rounded corners
        """
        if rounded:
            points = ((left, top), (left + width, top), (left + width, top + height), (left, top + height))

            radius = min(width, height) / 10

            pygame.draw.line(self.DISPLAYSURF, color, (points[0][0] + math.floor(radius / 2), points[0][1]), (points[1][0] - math.floor(radius / 2), points[1][1]), thickness)
            pygame.draw.line(self.DISPLAYSURF, color, (points[1][0], points[1][1] + math.floor(radius / 2)), (points[2][0], points[2][1] - math.floor(radius / 2)), thickness)
            pygame.draw.line(self.DISPLAYSURF, color, (points[3][0] + math.floor(radius / 2), points[3][1]), (points[2][0] - math.floor(radius / 2), points[2][1]), thickness)
            pygame.draw.line(self.DISPLAYSURF, color, (points[0][0], points[0][1] + math.floor(radius / 2)), (points[3][0], points[3][1] - math.floor(radius / 2)), thickness)

            rectangles = (pygame.Rect((points[1][0] - radius - math.floor(thickness / 2) + 2 - thickness % 2, points[1][1] - math.floor(thickness / 2) + 1), (radius + thickness, radius + thickness)),
                          pygame.Rect((points[0][0] - math.floor(thickness / 2) + 1, points[0][1] - math.floor(thickness / 2) + 1), (radius + thickness, radius + thickness)),
                          pygame.Rect((points[3][0] - math.floor(thickness / 2) + 1, points[3][1] - radius - math.floor(thickness / 2) + 2 - thickness % 2), (radius + thickness, radius + thickness)),
                          pygame.Rect((points[2][0] - radius - math.floor(thickness / 2) + 2 - thickness % 2, points[2][1] - radius - math.floor(thickness / 2) + 2 - thickness % 2), (radius + thickness, radius + thickness)),
                          )

            pygame.draw.arc(self.DISPLAYSURF, color, rectangles[0], math.radians(0), math.radians(90), thickness)
            pygame.draw.arc(self.DISPLAYSURF, color, rectangles[1], math.radians(90), math.radians(180), thickness)
            pygame.draw.arc(self.DISPLAYSURF, color, rectangles[2], math.radians(180), math.radians(270), thickness)
            pygame.draw.arc(self.DISPLAYSURF, color, rectangles[3], math.radians(270), math.radians(360), thickness)
        else:
            rectangle = pygame.Rect(left, top, width, height)
            pygame.draw.rect(self.DISPLAYSURF, color, rectangle, thickness)

    def text(self, left, top, message, size, color, font=None, antialias=False, background=None):
        """Draw text.

        Keyword arguments:
        left -- x-coordinate (left-most is 0)
        top -- y-coordtinate (top-most is 0)
        message -- Message to be displayed
        size -- Size of the characters to be displayed
        color -- Color of the characters to be displayed
        font -- Font of the message
        antialias -- If True, the text uses antialiasing
        background -- If given, specifies the background color of the message
        """

        if not font:
            try:
                font = MAIN_FONTS["8bit"]
            except KeyError as e:
                logging.error(f"KeyError: {e} is not a valid key for 'FONTS' dict")
                return

        try:
            display_info = pygame.display.Info()

            display_width, display_height = display_info.current_w, display_info.current_h

            text_font = pygame.font.Font(font, round(size * display_height / 1080))
        except FileNotFoundError as e:
            logging.error(f"FileNotFoundError: {e}")
        else:
            text_renderer = text_font.render(message, antialias, color, background)

            self.DISPLAYSURF.blit(text_renderer, (left, top))
