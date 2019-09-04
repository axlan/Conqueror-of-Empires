# Ben-Ryder 2019

import pygame

import project.game.gui as gui
import project.menus.leaderboard as leaderboard
import project.data as data
import paths
from project.game.fog_model import Model


class Controller:
    """ the game creator object, Holds the model and view object, and runs the game."""
    def __init__(self, display, level):
        self.state = "game"
        self.display = display

        # General Game Setup
        self.game_model = Model(level)

        # View + GUI Setup
        self.GUI = gui.GameGui(self, self.display, self.game_model)

    def play(self):
        self.state = self.GUI.run()  # at finish, return new state wanted, either menu, quit or ended (game finished)
        if self.state != "ended":
            self.quit()
            return self.state  # focus ends, back to main program controller to deal with new state
        else:
            return "quit"

    def get_state(self):
        return self.state
