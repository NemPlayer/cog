import pygame
import math

class Window:
    """Creates a window."""

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self):
        """Constructor of Window class."""

        pygame.init()

        self.DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def fill(self, color, rect=None, special_flags=0):
        """Fill 'DISPLAYSURF' with a solid color.

        Keyword arguments:
        color -- Color with which 'DISPLAYSURF' is filled
        rect -- If given, limits the fill to a specific area
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
        thickness -- If given, used for line thickness or to indicate that the rectangle is to be filled
        rounded -- If True, the rectangle has rounded corners
        """
        if rounded:
            points = ((left, top), (left + width, top), (left + width, top + height), (left, top + height))

            radius = (width + height) * 0.1

            pygame.draw.line(self.DISPLAYSURF, color, (points[0][0] + radius // 2, points[0][1]), (points[1][0] - radius // 2, points[1][1]), thickness)
            pygame.draw.line(self.DISPLAYSURF, color, (points[1][0], points[1][1] + radius // 2), (points[2][0], points[2][1] - radius // 2), thickness)
            pygame.draw.line(self.DISPLAYSURF, color, (points[3][0] + radius // 2 - 1, points[3][1]), (points[2][0] - radius // 2, points[2][1]), thickness)
            pygame.draw.line(self.DISPLAYSURF, color, (points[0][0], points[0][1] + radius // 2 - 1), (points[3][0], points[3][1] - radius // 2), thickness)

            rectangles = (pygame.Rect(left, top, radius, radius),
                          pygame.Rect(left + width - radius, top, radius, radius),
                          pygame.Rect(left + width - radius, top + height - radius, radius, radius),
                          pygame.Rect(left, top + height - radius, radius, radius),
                          )

            pygame.draw.arc(self.DISPLAYSURF, color, rectangles[0], math.radians(90), math.radians(180), thickness)
            pygame.draw.arc(self.DISPLAYSURF, color, rectangles[1], math.radians(0), math.radians(90), thickness)
            pygame.draw.arc(self.DISPLAYSURF, color, rectangles[2], math.radians(270), math.radians(360), thickness)
            pygame.draw.arc(self.DISPLAYSURF, color, rectangles[3], math.radians(180), math.radians(270), thickness)
        else:
            rectangle = pygame.Rect(left, top, width, height)
            pygame.draw.rect(self.DISPLAYSURF, color, rectangle, thickness)
