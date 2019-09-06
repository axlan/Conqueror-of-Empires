# Ben-Ryder 2019

import constants
import paths

import pygame
import project.menus as menus
import project.game.controller as game
from project.game.level_data import LevelData
from project.game.fog_model import Player


class ApplicationController:
    """ runs the whole application, changing section running based on state """
    def __init__(self):
        pygame.init()

        # Icon Setup
        icon = pygame.image.load(paths.uiMenuPath + "logo.png")
        icon.set_colorkey((0, 0, 0))
        pygame.display.set_icon(icon)  # before set_mode as suggested in pygame docs

        # Display Setup
        self.display = pygame.display.set_mode(constants.DISPLAY_SIZE)
        pygame.display.set_caption(constants.DISPLAY_NAME)

        # General Setup
        self.game_reference = None
        self.player = None
        self.level = 'demo'
        self.state = "info_dump"


    def run(self):
        
        self.player = Player('player', 'green')
        while self.state != "quit":
            
            self.level_data = LevelData.parse_file(paths.levelPath + self.level + '.json')

            if self.state == "info_dump":
                self.run_info_dump()
            elif self.state == "shop":
                self.run_shop()
            elif self.state == "tactics":
                self.run_tactics()
            else:
                raise Exception("Invalid Game State: %s" % self.state)

        self.quit()

    def run_shop(self):
        menu = menus.DemoShop(self.display, self.player, self.level_data)
        self.state = menu.get_state()

    def run_info_dump(self):
        menu = menus.InfoDump(self.display, self.level_data)  # takes control while section running, control returns here after.
        self.state = menu.get_state()

    def run_tactics(self):
        running_game = game.Controller(self.display, self.player, self.level_data)
        self.state = running_game.play()  # takes control, returns when game is complete.
        self.game_reference = None

    def quit(self):
        pygame.quit()
        quit()
        
