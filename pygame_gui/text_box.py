

# Ben-Ryder 2019

import pygame
from pygame_gui.text import Text
from pygame_gui.text_style import TextStyle
from enum import Enum, auto

class TextAlignmentHoriz(Enum):
    LEFT = auto()
    RIGHT = auto()
    CENTER = auto()

class TextAlignmentVert(Enum):
    TOP = auto()
    BOTTOM = auto()
    CENTER = auto()



def draw_box(surface: pygame.Surface, rect: pygame.Rect, background_color: pygame.Color=None, border_color: pygame.Color=None, border_size=0):
    pygame.draw.rect(surface, border_color, rect)
    # just calling pygame.draw.rect with the width sometimes dropped pixels
    r = pygame.Rect(rect.x + border_size, rect.y + border_size, rect.width - border_size * 2, rect.height - border_size * 2)
    pygame.draw.rect(surface, background_color, r)

class TextBox:
    def __init__(self, text: str, rect: pygame.Rect, text_style: TextStyle, alignment_horiz=TextAlignmentHoriz.LEFT, alignment_vert=TextAlignmentVert.TOP, padding=0, background_color: pygame.Color=None, border_color: pygame.Color=None, border_size=0):
        self.text = text
        self.rect = rect
        self.text_style = text_style
        self.alignment_horiz = alignment_horiz
        self.alignment_vert = alignment_vert
        self.padding = padding
        self.background_color = background_color
        self.border_color = border_color
        self.border_size = border_size
        self.graphic = None
        self._config_graphic()

    def _config_graphic(self):
        text_obj = Text(self.text, self.text_style.size, self.text_style.color, self.text_style.font, 0, 0)
        offset = self.padding + self.border_size
        if self.rect.width == 0:
            self.rect.width = text_obj.get_rect().width + offset * 2
            self.rect.height = text_obj.get_rect().height + offset * 2
        self.graphic = pygame.Surface((self.rect.width, self.rect.height))
        r = pygame.Rect(0, 0, self.rect.width, self.rect.height)
        draw_box(self.graphic, r, self.background_color, self.border_color, self.border_size)
        r = pygame.Rect(0, 0, text_obj.get_rect().width, text_obj.get_rect().height)
        if self.alignment_horiz == TextAlignmentHoriz.LEFT:
            r.left = offset
        elif self.alignment_horiz == TextAlignmentHoriz.CENTER:
            r.centerx = self.rect.width / 2
        else:
            r.right = offset
        if self.alignment_vert == TextAlignmentVert.TOP:
            r.top = offset
        elif self.alignment_vert == TextAlignmentVert.CENTER:
            r.centery = self.rect.height / 2
        else:
            r.bottom = offset
        text_obj.x = r.x
        text_obj.y = r.y
        #     text_obj.rect.
        text_obj.draw(self.graphic)

    def get_rect(self):
        return self.rect

    def change_text(self, text):
        self.text = text
        self._config_text()

    def draw(self, display):
        display.blit(self.graphic, [self.rect.x, self.rect.y])
