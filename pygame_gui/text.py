# Ben-Ryder 2019

import pygame


class Text:
    def __init__(self, text, size, colour, font, x, y):
        self.text_lines = text.split('\n')
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.font = font
        self._config_font()
        self._config_text()

    def _config_font(self):
        try:
            self.graphic_font = pygame.font.Font(self.font, self.size)
        except OSError:  # can't read font file.
            self.graphic_font = pygame.font.SysFont(self.font, self.size)

    def _config_text(self):
        graphic_texts = [ self.graphic_font.render(text, True, self.colour) for text in self.text_lines ]
        line_height = max([ text.get_rect().height for text in graphic_texts ])
        line_width = max([ text.get_rect().width for text in graphic_texts ])
        self.graphic_text = pygame.Surface((line_width, line_height * len(graphic_texts)), flags=pygame.SRCALPHA)
        for i, text in enumerate(graphic_texts):
            y = i * line_height
            self.graphic_text.blit(text, [0, y])
        self.rect = self.graphic_text.get_rect().move(self.x, self.y)

    def get_rect(self):
        return self.rect

    def change_text(self, text):
        self.text = text
        self._config_text()

    def draw(self, display):
        display.blit(self.graphic_text, [self.x, self.y])
