

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

    def __init__(self, items, resources, rect):
        self.items = items
        self.rect = rect
        self.sel = None
        self.resources = resources
        self.buy_buttons = []
        self.bought = []
        self.done = False
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
        r = pygame.Rect(0, 0, 100, 25)
        r.right = self.rect.x + self.rect.width
        r.bottom = self.rect.y + self.rect.height
        self.done_button = TextButton(r, 150, 200, 'Done', 18, constants.DIALOG_PANEL_SETTING_STYLE.color, constants.DIALOG_PANEL_SETTING_STYLE.font)


        setting_box.draw(self.graphic)
        options_box.draw(self.graphic)
        self._update_description()


    def get_rect(self):
        return self.rect

    def handle_click(self):
        if self.done_button.check_clicked():
            self.done = True
        for i, button in enumerate(self.buy_buttons):
            if i not in self.bought and self.items[i][1] <= self.resources.cash and button.mouse_over():
                self.bought.append(i)
                self.resources.cash -= self.items[i][1]
                self.resources.purchases.append(self.items[i][0])
            

    def draw(self, display):
        display.blit(self.graphic, [self.rect.x, self.rect.y])
        resource_text = Text(f'Money Available: {self.resources.cash}',
                              constants.DIALOG_PANEL_SETTING_STYLE.size,
                              constants.DIALOG_PANEL_SETTING_STYLE.color,
                              constants.DIALOG_PANEL_SETTING_STYLE.font,
                              0, 0)
        resource_text.x = self.rect.width - resource_text.get_rect().width - 5
        resource_text.draw(display)
        self.done_button.draw(display)
        hover = False
        for i, button in enumerate(self.buy_buttons):
            button.draw(display)
            if button.mouse_over():
                hover = True
                if i is not None and i != self.sel:
                     self.sel = i
                     self._update_description()
            if not hover and self.sel is not None:
                self.sel = None
                self._update_description()
            if i in self.bought:
                sold_text = Text(f'Sold Out',
                                constants.DIALOG_PANEL_SETTING_STYLE.size + 6,
                                Color('red'),
                                constants.DIALOG_PANEL_SETTING_STYLE.font,
                                100 + self.rect.x, 30 * (1 + i) + self.rect.y)
                sold_text.draw(display)

