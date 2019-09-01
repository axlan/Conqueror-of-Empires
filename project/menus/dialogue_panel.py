
# [Setting]
# [name]: [portrait]
# [Text]

# [Next]


# Ben-Ryder 2019

import pygame
import pygame_gui
from pygame_gui.panel import Panel
from pygame_gui.text import Text
from pygame_gui.text_button import TextButton
from pygame_gui.text_box import TextBox, TextAlignmentHoriz, TextAlignmentVert
import constants
from pygame import Rect, Color

class DialoguePanel:
    def __init__(self, setting, script, rect):
        self.script = script
        self.rect = rect
        self.setting = setting
        self.page = 0
        self.done = False
        self.next_button = None
        self.graphic = None
        self._construct_graphic()


    def _construct_graphic(self):
        self.graphic = pygame.Surface((self.rect.width, self.rect.height))
        y = 0
        setting_box = TextBox(self.setting,
                              Rect(0, y, self.rect.width, 25),
                              constants.DIALOG_PANEL_SETTING_STYLE,
                              TextAlignmentHoriz.CENTER,
                              TextAlignmentVert.CENTER,
                              background_color=constants.DIALOG_PANEL_BACKGROUND,
                              border_color=constants.DIALOG_PANEL_BORDER,
                              border_size=2)
        y += 25
        speaker = constants.CHAR_DIALOGUE_MAP[self.script[self.page][0]]
        speaker_img = pygame_gui.Image(speaker[0], 0, y, 100, 100)
        speaker_title = TextBox(self.script[self.page][0],
                              Rect(speaker_img.rect.width, y, 0, 0),
                              constants.DIALOG_PANEL_SETTING_STYLE,
                              TextAlignmentHoriz.CENTER,
                              TextAlignmentVert.CENTER,
                              background_color=constants.DIALOG_PANEL_BACKGROUND,
                              border_color=constants.DIALOG_PANEL_BORDER,
                              border_size=2)
        # will be drawn on target surface each time so needs to account for self.rect offset
        y += speaker_img.rect.height
        dialogue_box = TextBox(self.script[self.page][1],
                              Rect(0, y, self.rect.width, self.rect.height - y),
                              constants.DIALOG_PANEL_SETTING_STYLE,
                              background_color=constants.DIALOG_PANEL_BACKGROUND,
                              border_color=constants.DIALOG_PANEL_BORDER,
                              border_size=2)
        r = pygame.Rect(0, 0, 100, 25)
        r.right = self.rect.x + self.rect.width
        r.bottom = self.rect.y + self.rect.height
        self.next_button = TextButton(r, 150, 200, 'Next', 18, constants.DIALOG_PANEL_SETTING_STYLE.color, constants.DIALOG_PANEL_SETTING_STYLE.font)


        setting_box.draw(self.graphic)
        speaker_img.draw(self.graphic)
        speaker_title.draw(self.graphic)
        dialogue_box.draw(self.graphic)


    def get_rect(self):
        return self.rect

    def handle_click(self):
        if self.next_button.check_clicked():
            if self.page < len(self.script) - 1:
                self.page += 1
                self._construct_graphic()
            else:
                self.done = True
            

    def draw(self, display):
        display.blit(self.graphic, [self.rect.x, self.rect.y])
        self.next_button.draw(display)