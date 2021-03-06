import pygame
import logging
import math
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

        display_info = pygame.display.Info()
        self.DISPLAY_WIDTH = display_info.current_w
        self.DISPLAY_HEIGHT = display_info.current_h

        # Simulate Display Resolution
        # self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = 1920, 400

    def fill(self, color, rect=None, special_flags=0):
        """Fill 'DISPLAYSURF' with a solid color.

        Keyword arguments:
        color -- Color with which the screen is filled
        rect -- If given, limits the fill to a specific area
        special_flag -- If given, controls the use of colors
        """

        self.DISPLAYSURF.fill(color, rect, special_flags)

    def rect(self, color, left, top,
             width, height, thickness=1, rounded=False):
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
            points = (
                (left, top),
                (left + width, top),
                (left + width, top + height),
                (left, top + height),
            )

            radius = min(width, height)/10

            pygame.draw.line(
                self.DISPLAYSURF,
                color,
                (points[0][0] + math.floor(radius/ 2), points[0][1]),
                (points[1][0] - math.floor(radius/ 2), points[1][1]),
                thickness
            )
            pygame.draw.line(
                self.DISPLAYSURF,
                color,
                (points[1][0], points[1][1] + math.floor(radius/ 2)),
                (points[2][0], points[2][1] - math.floor(radius/ 2)),
                thickness
            )
            pygame.draw.line(
                self.DISPLAYSURF,
                color,
                (points[3][0] + math.floor(radius/2), points[3][1]),
                (points[2][0] - math.floor(radius/2), points[2][1]),
                thickness
            )
            pygame.draw.line(
                self.DISPLAYSURF,
                color,
                (points[0][0], points[0][1] + math.floor(radius/2)),
                (points[3][0], points[3][1] - math.floor(radius/2)),
                thickness
            )

            rectangles = (
                pygame.Rect(
                    (
                        points[1][0] - radius - round(thickness/2 - 1),
                        points[1][1] - round(thickness/2 - 1)
                    ),
                    (
                        radius + thickness,
                        radius + thickness
                    )
                ),
                pygame.Rect(
                    (
                        points[0][0] - round(thickness/2 - 1),
                        points[0][1] - round(thickness/2 - 1)
                    ),
                    (
                        radius + thickness,
                        radius + thickness
                    )
                ),
                pygame.Rect(
                    (
                        points[3][0] - round(thickness/2 - 1),
                        points[3][1] - radius - round(thickness/2 - 1)
                    ),
                    (
                        radius + thickness,
                        radius + thickness
                    )
                ),
                pygame.Rect(
                    (
                        points[2][0] - radius - round(thickness/2 - 1),
                        points[2][1] - radius - round(thickness/2 - 1)
                    ),
                    (
                        radius + thickness,
                        radius + thickness
                    )
                ),
            )

            pygame.draw.arc(
                self.DISPLAYSURF, color, rectangles[0],
                math.radians(0), math.radians(90), thickness
            )
            pygame.draw.arc(
                self.DISPLAYSURF, color, rectangles[1],
                math.radians(90), math.radians(180), thickness
            )
            pygame.draw.arc(
                self.DISPLAYSURF, color, rectangles[2],
                math.radians(180), math.radians(270), thickness
            )
            pygame.draw.arc(
                self.DISPLAYSURF, color, rectangles[3],
                math.radians(270), math.radians(360), thickness
            )
        else:
            rectangle = pygame.Rect(left, top, width, height)
            pygame.draw.rect(self.DISPLAYSURF, color, rectangle, thickness)

    def text(self, left, top, message,
             size, color, font=None, antialias=False, background=None):
        """Draw text.

        Keyword arguments:
        left -- x-coordinate (left-most is 0)
        top -- y-coordtinate (top-most is 0)
        message -- Message to be displayed
        size -- Size of the characters to be displayed
        color -- Color of the characters to be displayed
        font -- Font of the message
        antialias -- If True, the text uses antialiasing
        background -- If given, specifies the background color
                      of the message
        """

        if not font:
            try:
                font = MAIN_FONTS["8bit"]
            except KeyError as e:
                logging.error(f"KeyError: {e} is not a valid key for 'FONTS'")
                return

        try:
            text_font = pygame.font.Font(
                font,
                round(size*self.DISPLAY_HEIGHT/1080)
            )
        except FileNotFoundError as e:
            logging.error(f"FileNotFoundError: {e}")
        else:
            text_renderer = text_font.render(
                message, antialias,
                color, background
            )

            self.DISPLAYSURF.blit(text_renderer, (left, top))
