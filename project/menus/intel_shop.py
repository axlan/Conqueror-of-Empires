

import pygame
import pygame_gui
from pygame_gui.panel import Panel
from pygame_gui.text import Text
from pygame_gui.text_button import TextButton
from pygame_gui.text_box import TextBox, TextAlignmentHoriz, TextAlignmentVert
import constants
from pygame import Rect, Color

class IntelShop:

    DESRIPTION_WIDTH = 400

    def __init__(self, items, rect):
        self.items = items
        self.rect = rect
        self.sel = None
        self.buy_buttons = []
        self.done_button = None
        self.graphic = None
        self._construct_graphic()


    def _update_description(self):
        y = 25
        if self.sel is None:
            text = ''
        else:
            text = self.items[self.sel][2]
        description_box = TextBox(text,
                        Rect(self.rect.width - IntelShop.DESRIPTION_WIDTH, y, IntelShop.DESRIPTION_WIDTH, self.rect.height - y),
                        constants.DIALOG_PANEL_SETTING_STYLE,
                        background_color=constants.DIALOG_PANEL_BACKGROUND,
                        border_color=constants.DIALOG_PANEL_BORDER,
                        border_size=2)
        description_box.draw(self.graphic)

    def _construct_graphic(self):
        self.graphic = pygame.Surface((self.rect.width, self.rect.height))
        y = 0
        setting_box = TextBox('Intel Expenditure Selection',
                              Rect(0, y, self.rect.width, 25),
                              constants.DIALOG_PANEL_SETTING_STYLE,
                              TextAlignmentHoriz.CENTER,
                              TextAlignmentVert.CENTER,
                              background_color=constants.DIALOG_PANEL_BACKGROUND,
                              border_color=constants.DIALOG_PANEL_BORDER,
                              border_size=2)
        y += 25
        options_box = TextBox('',
                              Rect(0, y, self.rect.width - IntelShop.DESRIPTION_WIDTH, self.rect.height - y),
                              constants.DIALOG_PANEL_SETTING_STYLE,
                              background_color=constants.DIALOG_PANEL_BACKGROUND,
                              border_color=constants.DIALOG_PANEL_BORDER,
                              border_size=2)
        y += 5
        for item in self.items:
            r = Rect(10, y, 300, 25)
            self.buy_buttons.append(TextButton(
                r,
                150, 200,
                f'{item[0]}: ${item[1]}',
                18, constants.DIALOG_PANEL_SETTING_STYLE.color, constants.DIALOG_PANEL_SETTING_STYLE.font
            ))
            y += 30

        setting_box.draw(self.graphic)
        options_box.draw(self.graphic)
        self._update_description()


    def get_rect(self):
        return self.rect

    def handle_click(self):
        pass
        # if self.next_button.check_clicked():
        #     if self.page < len(self.script) - 1:
        #         self.page += 1
        #         self._construct_graphic()
        #     else:
        #         self.done = True
            

    def draw(self, display):
        display.blit(self.graphic, [self.rect.x, self.rect.y])
        for i, button in enumerate(self.buy_buttons):
            button.draw(display)
            hover = False
            if button.mouse_over():
                hover = True
                if i is not None and i != self.sel:
                     self.sel = i
                     self._update_description()
            if not hover and self.sel is not None:
                self.sel = None
                self._update_description()

