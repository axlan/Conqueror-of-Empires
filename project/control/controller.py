# Ben-Ryder 2019

import constants
import paths

import pygame
import project.menus as menus
import project.game.controller as game


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
        self.state = "info_dump"
        self.game_reference = None
        self.resources = None

    def run(self):
        while self.state != "quit":
            
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
        menu = menus.DemoShop(self.display)
        self.state = menu.get_state()
        self.resources = menu.resources

    def run_info_dump(self):
        menu = menus.InfoDump(self.display)  # takes control while section running, control returns here after.
        self.state = menu.get_state()

    def run_tactics(self):
        level = 'demo1'
        running_game = game.Controller(self.display, level)
        self.state = running_game.play()  # takes control, returns when game is complete.
        self.game_reference = None

    def quit(self):
        pygame.quit()
        quit()
        
