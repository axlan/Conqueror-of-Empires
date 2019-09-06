# Ben-Ryder 2019
import pygame

import paths
import constants

import pygame_gui
from project.menus.dialogue_panel import DialoguePanel
from project.game.level_data import LevelData

class InfoDump:
    """ top section for user to pick state. new_game, leaderboard ..."""
    def __init__(self, display: pygame.Surface, level: LevelData):
        self.display = display
        self.state = "info_dump"
        self.game_reference = None

        self.dialog_panel = DialoguePanel(level.brief_setting,
                                          level.brief_pages,
                                          pygame.Rect(0, 0, 800, 600))


        self.run()

    def run(self):
        while self.state == "info_dump":
            self.handle_events()
            self.draw()

    def get_state(self):
        return self.state

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "quit"

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.dialog_panel.handle_click()
                if self.dialog_panel.done:
                    self.state = "shop"

                

    def draw(self):
        self.display.fill(pygame.Color('black'))
        self.dialog_panel.draw(self.display)
        pygame.display.update()

